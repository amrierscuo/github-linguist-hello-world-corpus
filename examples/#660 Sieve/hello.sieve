require ["fileinto"];
if header :is "Subject" "Hello, World!" {
    fileinto "INBOX.CorpusGreeting";
    stop;
} else {
    keep;
}
