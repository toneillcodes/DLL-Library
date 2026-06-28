# Binary Specification: easwrt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\easwrt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a1d72033f3774968a74c8b733269d8754e6ac4a9e0b81b773e0defc6823b2929`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `EasClientSecurityPolicyApply` | `0x33B0` | 148 | UnwindData |  |
| 5 | `EasClientSecurityPolicyCheckCompliance` | `0x3450` | 148 | UnwindData |  |
| 6 | `EasGetClientDeviceInformation` | `0x34F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `EasShowConsentDialog` | `0x3510` | 546 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x4A40` | 85 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x4AA0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4AE0` | 134 | UnwindData |  |
| 7 | `EasRegisterEncryptionProvider` | `0x12680` | 128 | UnwindData |  |
| 9 | `EasUnRegisterEncryptionProvider` | `0x12710` | 145 | UnwindData |  |
