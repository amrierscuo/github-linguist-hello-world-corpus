fn main(){
 let input=std::fs::read_to_string(std::env::args().nth(1).expect("WGSL path")).unwrap();
 let module=naga::front::wgsl::parse_str(&input).unwrap();
 naga::valid::Validator::new(naga::valid::ValidationFlags::all(),naga::valid::Capabilities::all()).validate(&module).unwrap();
 assert_eq!(module.entry_points[0].name,"main");
 assert_eq!(module.entry_points[0].workgroup_size,[13,1,1]);
 println!("PASS: genuine Naga WGSL parser and validator; GPU execution/readback pending");
}
