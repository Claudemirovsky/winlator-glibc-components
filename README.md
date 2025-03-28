# Winlator GLIBC Components

The idea behind this repo is to provide up-to-date components for 
[longjunyu2's Winlator GLIBC](https://github.com/longjunyu2/winlator).

The reason being, most providers of .WCP ("winlator component package"?) files
are kinda fishy: They don't show from where they're getting the binaries or how
they've compilled it, nor the source code used or patches applied (if any).
Also, most(if not ALL) of the uploads of .WCP files are done manually, via
github web, which absolutely sucks.

So, in this repo, I'm going to write some github workflows to automatize those updates
and push them to the [components](../components/) branch.

<details>
  <summary>What about the initial components, not uploaded by the workflows?</summary>

The initial components (not built by me) were uploaded manually, but they're from
_reasonably_ reliable sources:

- [BOX64](https://github.com/ptitSeb/box64): [Winlator GLIBC](https://github.com/longjunyu2/winlator/tree/main/installable_components/box64)
- [DXVK](https://github.com/doitsujin/dxvk): [OG Winlator](https://github.com/brunodev85/winlator/tree/main/installable_components/dxvk)
- [Turnip](https://gitlab.freedesktop.org/Pipetto-crypto/mesa/-/tree/winlator_wsi-termux-x11): [Winlator GLIBC](https://github.com/longjunyu2/winlator/tree/main/installable_components/turnip)
- [VKD3D](https://gitlab.winehq.org/wine/vkd3d): [OG Winlator](https://github.com/brunodev85/winlator/tree/main/installable_components/vkd3d)

</details>

## TODO

- [x] BOX64
  - [x] Create WCPs from the latest release
    - [x] Schedule weekly updates
  - [x] Create WCPs from the master branch
- [x] DXVK
  - [x] Create WCPs from the latest release
  - [x] Create WCPs from the github artifacts
    - [x] Schedule weekly updates
  - [x] Create [GPLASYNC](https://gitlab.com/Ph42oN/dxvk-gplasync/) WCPs
- [ ] VKD3D
  - [ ] [Original VKD3D](https://gitlab.winehq.org/wine/vkd3d): Create WCPs from the latest release
    - ~~Jesus Christ, OG VKD3D absolutely sucks to compile and distribute. if only it were as easy as vkd3d-proton....~~
  - [x] [VKD3D-PROTON](https://github.com/HansKristian-Work/vkd3d-proton): Create WCPs from the github artifacts
    - [x] Schedule weekly updates
  - [x] [VKD3D-PROTON](https://github.com/HansKristian-Work/vkd3d-proton): Create WCPs from the latest release
- [x] TURNIP
  - [x] Compile and create WCPs
