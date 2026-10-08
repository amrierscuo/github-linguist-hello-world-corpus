entity constant_greeting is port (message : out string(1 to 13)); end;
architecture wires of constant_greeting is begin message <= "Hello, World!"; end;
entity greeting_netlist is port (message : out string(1 to 13)); end;
architecture structural of greeting_netlist is begin
  u_message : entity work.constant_greeting port map (message => message);
end;
