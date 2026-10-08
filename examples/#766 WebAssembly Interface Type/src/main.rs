fn main(){
 let path=std::env::args().nth(1).expect("WIT path");
 let mut resolve=wit_parser::Resolve::default();
 let (package,_)=resolve.push_path(&std::path::Path::new(&path)).unwrap();
 assert_eq!(resolve.packages[package].name.namespace,"corpus");
 assert!(resolve.packages[package].worlds.contains_key("greeting"));
 println!("PASS: official wit-parser resolves greeter interface/world; component implementation and Hello, World! execution pending");
}
