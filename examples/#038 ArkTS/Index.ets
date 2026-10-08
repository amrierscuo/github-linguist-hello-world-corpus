@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello, World!')
        .fontSize(24)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
