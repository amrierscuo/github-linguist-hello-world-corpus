entity hello is
end entity;
architecture simulation of hello is
begin
    process
    begin
        report "Hello, World!" severity note;
        wait;
    end process;
end architecture;
