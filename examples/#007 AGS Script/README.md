# #007 AGS Script

`room1.asc` is a room script for **Adventure Game Studio (AGS)**.
`room_AfterFadeIn` operator shows `Hello, World!` in the message window after
The call is blocking until the player closes the room.
messaggio.

## Toolchain and commands

Serves **AGS Editor 3.6.x** and its game engine. Create a project from
a template with an initial room and the configured character. Open the
script of the initial room and enter the content of `room1.asc`.

In the Events properties of the room connect `Enters room after fade-in` to the
`room_AfterFadeIn` function. The function name alone does not establish the
link for a room event. If the template already has the manager,
add the `Display` call without defining two functions.

Comando reale di compilazione: `Build > Build EXE` nell'AGS Editor. Comando di
execution of the game compiled on Windows: `Compiled/Windows/<nome_gioco>.exe`,
where `<nome_gioco>` is the Game file name of the host project.
window with `Hello, World!` at the entrance into the room, after the fade-in.

The `.asc` file is the source drive of the example; this folder does not contain
a complete AGS project, pictures, binary room or a compiled game.

## Status and limitations

Artifact created; syntax and behavior **non ancora verificate** by compiler
and from the AGS engine. Editor, host project and resources are not available in this
sessione.

## Official sources

- [AGS, funzione `Display`](https://adventuregamestudio.github.io/ags-manual/Globalfunctions_Message.html).
- [AGS, eventi della stanza e `room_AfterFadeIn`](https://adventuregamestudio.github.io/ags-manual/EventTypes.html).
- [AGS, distribuzione e `Build EXE`](https://adventuregamestudio.github.io/ags-manual/DistGame.html).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asc` | [room1.asc](room1.asc), [greeting.asc](variants/ext-ash-2e617368/greeting.asc) created; verification pending |
| `.ash` | [hello.ash](variants/ext-ash-2e617368/hello.ash) created; verification pending |
