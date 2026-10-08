use serde::Deserialize;
#[derive(Deserialize)]
struct Greeting { greeting: String }
fn main() {
 let value: Greeting = ron::from_str(&std::fs::read_to_string("hello.ron").unwrap()).unwrap();
 assert_eq!(value.greeting, "Hello, World!");
 println!("{}", value.greeting);
}
