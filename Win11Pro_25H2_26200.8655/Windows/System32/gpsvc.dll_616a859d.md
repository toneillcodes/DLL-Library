# Binary Specification: gpsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\gpsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `616a859de60487f93a82610598c7dcf2f9f12df5c370c155199e13ba16bcb603`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 107 | `GroupPolicyClientServiceMain` | `0x27D30` | 407 | UnwindData |  |
| 108 | `SvchostPushServiceGlobals` | `0x5FAC0` | 75,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ProcessGroupPolicyCompletedExInternal` | `0x72310` | 3,507 | UnwindData |  |
| 111 | `GenerateRsopPolicy` | `0x992C0` | 4,219 | UnwindData |  |
| 113 | `ProcessGroupPolicyCompletedInternal` | `0x9FE40` | 45,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `DllCanUnloadNow` | `0xAB190` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `DllGetClassObject` | `0xAB1C0` | 253 | UnwindData |  |
| 114 | `RsopAccessCheckByTypeInternal` | `0xADA30` | 887 | UnwindData |  |
| 115 | `RsopFileAccessCheckInternal` | `0xADDB0` | 625 | UnwindData |  |
| 106 | *Ordinal Only* | `0xAE030` | 303 | UnwindData |  |
| 116 | `RsopResetPolicySettingStatusInternal` | `0xAE170` | 1,275 | UnwindData |  |
| 117 | `RsopSetPolicySettingStatusInternal` | `0xAE680` | 4,526 | UnwindData |  |
