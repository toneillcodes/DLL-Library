# Binary Specification: vbsapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vbsapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `09a876db27770e58a8aba6f3eaf723fbf181fa90fad5ab733dcd46cd21a736c3`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `VbsGetIssues` | `0x2300` | 71 | UnwindData |  |
| 18 | `VbsGetIssuesForWindowsPath` | `0x2350` | 216 | UnwindData |  |
| 19 | `VbsIsCapable` | `0x2690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `HvciIsRecommended` | `0x26B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `VbsIsRecommended` | `0x26B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `VbsIsScenarioEnabled` | `0x26C0` | 59 | UnwindData |  |
| 22 | `VbsIsVbsRecommended` | `0x2710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `VbsSetKernelShadowStacksScenarioEnable` | `0x2730` | 164 | UnwindData |  |
| 24 | `VbsSetKernelShadowStacksScenarioEnableToVBSKey` | `0x27E0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `VbsSetScenarioEnable` | `0x28F0` | 162 | UnwindData |  |
| 26 | `VbsSetScenarioEnableToVBSKey` | `0x29A0` | 42,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `HvciGetConfig` | `0xD010` | 115 | UnwindData |  |
| 2 | `HvciGetConfigFromVBSKey` | `0xD090` | 117 | UnwindData |  |
| 3 | `HvciIncompatibilityScanCancel` | `0xD110` | 82 | UnwindData |  |
| 4 | `HvciIncompatibilityScanFree` | `0xD170` | 107 | UnwindData |  |
| 5 | `HvciIncompatibilityScanGetResult` | `0xD1F0` | 38 | UnwindData |  |
| 6 | `HvciIncompatibilityScanInitialize` | `0xD220` | 261 | UnwindData |  |
| 7 | `HvciIncompatibilityScanInitialize2` | `0xD330` | 202 | UnwindData |  |
| 8 | `HvciIncompatibilityScanOverrideDriverCompatDatabase` | `0xD400` | 59 | UnwindData |  |
| 9 | `HvciIncompatibilityScanOverrideServicesKey` | `0xD450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HvciIncompatibilityScanStart` | `0xD460` | 133 | UnwindData |  |
| 11 | `HvciIsActive` | `0xD4F0` | 109 | UnwindData |  |
| 13 | `KernelShadowStacksGetConfig` | `0xD570` | 132 | UnwindData |  |
| 14 | `KernelShadowStacksGetConfigFromVBSKey` | `0xD600` | 301 | UnwindData |  |
| 15 | `KernelShadowStacksIsActive` | `0xD740` | 94 | UnwindData |  |
| 16 | `KernelShadowStacksIsCapable` | `0xD7B0` | 145 | UnwindData |  |
