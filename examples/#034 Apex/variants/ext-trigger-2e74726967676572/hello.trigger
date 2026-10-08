trigger CorpusGreeting on Account (before insert) {
    for (Account record : Trigger.new) { record.Description = 'Hello, World!'; }
}
