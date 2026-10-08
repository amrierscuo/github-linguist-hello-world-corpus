import java.io.ByteArrayOutputStream;
import java.io.File;
import org.apache.avro.Protocol;
import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericDatumWriter;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DecoderFactory;
import org.apache.avro.io.EncoderFactory;

class AvroCheck {
  public static void main(String[] args) throws Exception {
    Protocol protocol = Protocol.parse(new File(args[0]));
    Schema schema = protocol.getType("Greeting");
    Object value = GenericData.get().getDefaultValue(schema.getField("message"));
    if (!value.toString().equals("Hello, World!")) throw new AssertionError("Wrong default");
    GenericRecord record = new GenericData.Record(schema);
    record.put("message", value);
    ByteArrayOutputStream bytes = new ByteArrayOutputStream();
    var encoder = EncoderFactory.get().binaryEncoder(bytes, null);
    new GenericDatumWriter<GenericRecord>(schema).write(record, encoder);
    encoder.flush();
    GenericRecord decoded = new GenericDatumReader<GenericRecord>(schema).read(null,
        DecoderFactory.get().binaryDecoder(bytes.toByteArray(), null));
    if (!decoded.get("message").toString().equals("Hello, World!")) throw new AssertionError("Round trip failed");
    System.out.println(decoded.get("message"));
    System.out.println("PASS: compiled IDL default; genuine Avro binary encode/decode");
  }
}
