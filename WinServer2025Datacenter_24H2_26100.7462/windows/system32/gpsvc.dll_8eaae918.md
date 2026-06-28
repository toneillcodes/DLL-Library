# Binary Specification: gpsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gpsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8eaae918891503c911fe1ca9c61981fd23c78b43d79bf00275e0f7dde521efa7`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 107 | `GroupPolicyClientServiceMain` | `0x10440` | 407 | UnwindData |  |
| 108 | `SvchostPushServiceGlobals` | `0x5F8C0` | 71,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ProcessGroupPolicyCompletedExInternal` | `0x70EB0` | 3,507 | UnwindData |  |
| 111 | `GenerateRsopPolicy` | `0x95600` | 4,219 | UnwindData |  |
| 113 | `ProcessGroupPolicyCompletedInternal` | `0x9BE30` | 46,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `DllCanUnloadNow` | `0xA73A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `DllGetClassObject` | `0xA73D0` | 268 | UnwindData |  |
| 114 | `RsopAccessCheckByTypeInternal` | `0xA9F60` | 887 | UnwindData |  |
| 115 | `RsopFileAccessCheckInternal` | `0xAA2E0` | 625 | UnwindData |  |
| 106 | *Ordinal Only* | `0xAA560` | 303 | UnwindData |  |
| 116 | `RsopResetPolicySettingStatusInternal` | `0xAA6A0` | 1,275 | UnwindData |  |
| 117 | `RsopSetPolicySettingStatusInternal` | `0xAABB0` | 4,526 | UnwindData |  |
