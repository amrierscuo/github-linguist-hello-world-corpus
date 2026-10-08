entity main is end;
architecture test of main is
  signal message : string(1 to 13);
begin
  u_greeting : entity work.greeting port map (message => message);
  process begin wait for 1 ns; assert message = "Hello, World!" severity failure; report message severity note; wait; end process;
end;
