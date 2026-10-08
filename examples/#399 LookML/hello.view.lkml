view: hello {
  derived_table: {
    sql: SELECT 'Hello, World!' AS greeting ;;
  }
  dimension: greeting {
    type: string
    sql: ${TABLE}.greeting ;;
  }
}
