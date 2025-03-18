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

- BOX64: [Winlator GLIBC](https://github.com/longjunyu2/winlator/tree/main/installable_components/box64)
- DXVK: [OG Winlator](https://github.com/brunodev85/winlator/tree/main/installable_components/dxvk)
- Turnip: [Winlator GLIBC](https://github.com/longjunyu2/winlator/tree/main/installable_components/turnip)
- VKD3D: [OG Winlator](https://github.com/brunodev85/winlator/tree/main/installable_components/vkd3d)

</details>

## TODO

- [ ] BOX64
  - [x] Create WCPs from the latest release
    - [ ] Schedule weekly updates
  - [x] Create WCPs from the master branch
- [ ] DXVK
  - [ ] Create WCPs from the latest release
  - [ ] Create WCPs from the github artifacts
    - [ ] Schedule weekly updates
  - [ ] Create [GPLASYNC](https://gitlab.com/Ph42oN/dxvk-gplasync/) WCPs
- [ ] VKD3D
  - [ ] [Original VKD3D](https://gitlab.winehq.org/wine/vkd3d): Create WCPs from the latest release
  - [ ] [VKD3D-PROTON](https://github.com/HansKristian-Work/vkd3d-proton): Create WCPs from the github artifacts
    - [ ] Schedule weekly updates
  - [ ] [VKD3D-PROTON](https://github.com/HansKristian-Work/vkd3d-proton): Create WCPs from the latest release
- [ ] TURNIP
  - [ ] ~~Compile and create WCPs~~ (impossible for now, as [freedesktop's gitlab](https://gitlab.freedesktop.org/Pipetto-crypto/mesa/-/tree/winlator_wsi-termux-x11) is down)
  - [ ] Redistribute pre-built WCPs from [K1MMCH1's repo](https://github.com/K11MCH1/WinlatorTurnipDrivers)
