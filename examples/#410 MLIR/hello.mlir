module {
  llvm.mlir.global internal constant @message("Hello, World!\00")
  llvm.func @puts(!llvm.ptr) -> i32
  llvm.func @main() -> i32 {
    %message = llvm.mlir.addressof @message : !llvm.ptr
    %printed = llvm.call @puts(%message) : (!llvm.ptr) -> i32
    %zero = llvm.mlir.constant(0 : i32) : i32
    llvm.return %zero : i32
  }
}
