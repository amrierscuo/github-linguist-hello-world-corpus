namespace hello;

@greeting: 'Hello, World!'
entity Greeting {
  key ID : Integer;
  message : String(13) default 'Hello, World!';
}
