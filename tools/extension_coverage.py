"""Audit coverage of every canonical language-extension pair (stdlib only)."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
REFERENCE_HASH='183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043'
BASELINE_HASH='c628b8b39a4ed424e768cd1e67a63bba88de6b2ca7d65d48c4408641762e400b'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def require(test,message):
    if not test:raise ValueError(message)
def inside(relative):
    posix=PurePosixPath(relative)
    require(not posix.is_absolute() and '..' not in posix.parts and ':' not in relative and '\\' not in relative,'Unsafe path: '+relative)
    path=(ROOT/relative).resolve()
    require(path.is_relative_to(ROOT),'Path outside corpus: '+relative)
    return path

def audit():
    require(sha(ROOT/'reference/languages.yml')==REFERENCE_HASH,'Canonical YAML changed')
    baseline_path=ROOT/'tracking/extensions_baseline.json'
    require(sha(baseline_path)==BASELINE_HASH,'Frozen extension baseline changed')
    baseline=json.loads(baseline_path.read_text(encoding='utf-8'))
    require(baseline['reference_sha256']==REFERENCE_HASH,'Extension baseline reference mismatch')
    tracker=json.loads((ROOT/'tracking/languages_tracker.json').read_text(encoding='utf-8'))
    expected=[]
    for b,e in zip(baseline['entries'],tracker['entries']):
        require((b['ordinal'],b['name'],b['extensions'])==(e['ordinal'],e['name'],e['linguist']['extensions']),'Canonical language/extension mismatch')
        expected.extend((b['ordinal'],b['name'],ext) for ext in b['extensions'])
    require(len(baseline['entries'])==len(tracker['entries'])==836,'Expected 836 canonical languages')
    data=json.loads((ROOT/'tracking/extensions_tracker.json').read_text(encoding='utf-8'))
    require(data['reference_sha256']==REFERENCE_HASH,'Extension tracker reference mismatch')
    records=data['entries']
    require([(e['language_ordinal'],e['language_name'],e['extension']) for e in records]==expected,'Extension records must preserve every canonical pair in order')
    for item in records:
        e=tracker['entries'][item['language_ordinal']-1]
        files=item['files']
        require(all(isinstance(item[k],bool) for k in ['artifact_created','syntax_verified','semantic_verified']),'Invalid extension flags')
        require(not item['semantic_verified'] or item['syntax_verified'],'Semantics require syntax')
        require(not item['syntax_verified'] or item['artifact_created'],'Verification requires artifact')
        require(item['artifact_created']==bool(files),'Created extension must have primary files; blocked extensions must not')
        require(item['validation_command'] and item['expected_result'] and item['sources'],'Missing procedure/expected result/primary sources')
        require(bool(item.get('documentation')),'Missing extension documentation')
        for relative in [item['documentation'],*item.get('supporting_files',[])]:
            path=inside(relative)
            declared=relative in e['example']['files'] or relative==e['folder']+'/README.md'
            require(path.is_relative_to(inside(e['folder'])) and declared,'Undeclared/misplaced extension support file')
            require(path.is_file() and path.stat().st_size>0,'Missing/empty extension support file: '+relative)
        for relative in files:
            path=inside(relative)
            require(path.is_relative_to(inside(e['folder'])),'File in wrong language folder')
            require(relative in e['example']['files'],'Extension file not declared in language tracker')
            require(path.is_file() and path.stat().st_size>0,'Missing/empty extension artifact: '+relative)
            require(path.name.endswith(item['extension']),'Suffix mismatch: '+relative)
            require(path.name!='README.md' and '/verification/' not in relative,'Documentation/evidence counted as an artifact')
        if item['syntax_verified']:
            require(bool(item.get('verification_log')),'Verified extension needs a log')
            log=inside(item['verification_log']);require(log.is_file(),'Missing extension evidence log')
            hashes=item.get('verified_artifact_sha256',{})
            require(hashes and all(relative in hashes for relative in files),'No verified extension artifact hashes')
            for relative,digest in hashes.items():
                require(relative in e['example']['files'] and sha(inside(relative))==digest,'Verified extension bytes changed: '+relative)
        else:
            require(not item.get('verified_artifact_sha256'),'Unverified extension must not claim verified hashes')
    unique={i['extension'] for i in records}
    covered={i['extension'] for i in records if i['artifact_created']}
    result={
        'canonical_language_extension_pairs':len(records),
        'pairs_with_artifacts':sum(i['artifact_created'] for i in records),
        'pairs_without_artifacts':sum(not i['artifact_created'] for i in records),
        'syntax_verified_pairs':sum(i['syntax_verified'] for i in records),
        'semantic_verified_pairs':sum(i['semantic_verified'] for i in records),
        'distinct_extensions':len(unique),
        'distinct_extensions_with_primary_artifacts':len(covered),
        'distinct_extensions_without_primary_artifacts':len(unique-covered),
        'basis':'Original examples, drafts/templates and added variants count as artifacts; verification is separate and variant-specific.'}
    return data,result

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('action',choices=['audit','refresh']);args=parser.parse_args()
    data,result=audit();path=ROOT/'tracking/extensions_progress.json'
    if args.action=='refresh':path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    require(json.loads(path.read_text(encoding='utf-8'))==result,'Stale extension progress')
    print('OK: every canonical language-extension pair, folder, declared file, flag and evidence hash audited.')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    print('This audit does not execute language toolchains.')

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError) as error:raise SystemExit('EXTENSION AUDIT FAILED: '+str(error))
