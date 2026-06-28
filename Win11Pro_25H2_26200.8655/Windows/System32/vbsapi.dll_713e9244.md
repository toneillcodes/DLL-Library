# Binary Specification: vbsapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vbsapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `713e9244ed475c4d83fa6358c23796fcf2dad04eb1f27afc8476605f8802067a`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `VbsGetIssues` | `0x2310` | 71 | UnwindData |  |
| 18 | `VbsGetIssuesForWindowsPath` | `0x2360` | 216 | UnwindData |  |
| 19 | `VbsIsCapable` | `0x26A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `HvciIsRecommended` | `0x26C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `VbsIsRecommended` | `0x26C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `VbsIsScenarioEnabled` | `0x26D0` | 59 | UnwindData |  |
| 22 | `VbsIsVbsRecommended` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `VbsSetKernelShadowStacksScenarioEnable` | `0x2740` | 164 | UnwindData |  |
| 24 | `VbsSetKernelShadowStacksScenarioEnableToVBSKey` | `0x27F0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `VbsSetScenarioEnable` | `0x2900` | 162 | UnwindData |  |
| 26 | `VbsSetScenarioEnableToVBSKey` | `0x29B0` | 42,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `HvciGetConfig` | `0xD140` | 115 | UnwindData |  |
| 2 | `HvciGetConfigFromVBSKey` | `0xD1C0` | 117 | UnwindData |  |
| 3 | `HvciIncompatibilityScanCancel` | `0xD240` | 82 | UnwindData |  |
| 4 | `HvciIncompatibilityScanFree` | `0xD2A0` | 107 | UnwindData |  |
| 5 | `HvciIncompatibilityScanGetResult` | `0xD320` | 38 | UnwindData |  |
| 6 | `HvciIncompatibilityScanInitialize` | `0xD350` | 261 | UnwindData |  |
| 7 | `HvciIncompatibilityScanInitialize2` | `0xD460` | 202 | UnwindData |  |
| 8 | `HvciIncompatibilityScanOverrideDriverCompatDatabase` | `0xD530` | 59 | UnwindData |  |
| 9 | `HvciIncompatibilityScanOverrideServicesKey` | `0xD580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HvciIncompatibilityScanStart` | `0xD590` | 133 | UnwindData |  |
| 11 | `HvciIsActive` | `0xD620` | 109 | UnwindData |  |
| 13 | `KernelShadowStacksGetConfig` | `0xD6A0` | 132 | UnwindData |  |
| 14 | `KernelShadowStacksGetConfigFromVBSKey` | `0xD730` | 301 | UnwindData |  |
| 15 | `KernelShadowStacksIsActive` | `0xD870` | 94 | UnwindData |  |
| 16 | `KernelShadowStacksIsCapable` | `0xD8E0` | 145 | UnwindData |  |
