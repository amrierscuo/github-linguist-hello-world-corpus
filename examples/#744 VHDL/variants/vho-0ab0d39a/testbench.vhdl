entity greeting_tb is end;
architecture test of greeting_tb is signal message : string(1 to 13); begin
  u_message : entity work.greeting_netlist port map (message => message);
  process begin wait for 1 ns; assert message = "Hello, World!" severity failure; report message severity note; wait; end process;
end;
