# Binary Specification: XInputUap.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\XInputUap.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `495610905316d70f90e7922ee56cd3dfa74898bf6911789179e833117a2c1739`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `XInputEnable` | `0x8A50` | 4,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x9C10` | 371 | UnwindData |  |
| 3 | `XInputGetAudioDeviceIds` | `0xA080` | 415 | UnwindData |  |
| 4 | `XInputGetBatteryInformation` | `0xA230` | 358 | UnwindData |  |
| 5 | `XInputGetCapabilities` | `0xA3A0` | 336 | UnwindData |  |
| 6 | `XInputGetKeystroke` | `0xA500` | 56 | UnwindData |  |
| 7 | `XInputGetState` | `0xA540` | 317 | UnwindData |  |
| 8 | `XInputSetState` | `0xA690` | 411 | UnwindData |  |
