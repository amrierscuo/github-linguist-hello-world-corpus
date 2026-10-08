use rhai::Engine;
use std::sync::{Arc,Mutex};
fn main() -> Result<(), Box<dyn std::error::Error>> {
 let path=std::env::args().nth(1).expect("Rhai script path");
 let observed=Arc::new(Mutex::new(Vec::new()));
 let capture=observed.clone();
 let mut engine=Engine::new();
 engine.on_print(move |text| { println!("{}",text); capture.lock().unwrap().push(text.to_owned()); });
 let ast=engine.compile_file(path.into())?;
 engine.eval_ast::<()>(&ast)?;
 assert_eq!(*observed.lock().unwrap(),vec!["Hello, World!".to_string()]);
 println!("PASS: genuine Rhai compile and AST execution, print callback checked");
 Ok(())
}
