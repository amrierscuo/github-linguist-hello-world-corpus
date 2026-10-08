entity greeting is port (message : out string(1 to 13)); end entity;
architecture constant_message of greeting is begin message <= "Hello, World!"; end architecture;
