# Binary Specification: XInputUap.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\XInputUap.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5b4fe20e91400612b6d55212ba6ab64c5520987a3415132d9e3f21c2bffbf2d5`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `XInputEnable` | `0x8970` | 4,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x9AF0` | 371 | UnwindData |  |
| 3 | `XInputGetAudioDeviceIds` | `0x9F60` | 415 | UnwindData |  |
| 4 | `XInputGetBatteryInformation` | `0xA110` | 358 | UnwindData |  |
| 5 | `XInputGetCapabilities` | `0xA280` | 336 | UnwindData |  |
| 6 | `XInputGetKeystroke` | `0xA3E0` | 56 | UnwindData |  |
| 7 | `XInputGetState` | `0xA420` | 317 | UnwindData |  |
| 8 | `XInputSetState` | `0xA570` | 411 | UnwindData |  |
