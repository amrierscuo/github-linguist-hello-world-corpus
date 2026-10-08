class GreetingShader extends hxsl.Shader {
    public static inline var greeting:String = "Hello, World!";
    static var SRC = {
        @input var input:{position:Vec3};
        var output:{position:Vec4, color:Vec4};
        function vertex() {
            output.position = vec4(input.position, 1.0);
        }
        function fragment() {
            output.color = vec4(1.0, 1.0, 1.0, 1.0);
        }
    };
}
