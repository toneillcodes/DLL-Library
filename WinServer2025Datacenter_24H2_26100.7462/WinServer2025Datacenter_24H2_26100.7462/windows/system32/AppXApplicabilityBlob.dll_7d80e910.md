# Binary Specification: AppXApplicabilityBlob.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppXApplicabilityBlob.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7d80e910e65e3a9b02a1dc420ca34e470ae4190cbf11eec66be7c8a38b18af52`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `GetApplicabilityFactory` | `0x10030` | 92 | UnwindData |  |
| 7 | `IsXAP` | `0x11270` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IsAppx` | `0x112F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IsPreThresholdDesktop` | `0x11380` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IsPreThresholdPhone` | `0x11F40` | 68,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateSerializedBundleManifestStatement` | `0x22930` | 450 | UnwindData |  |
| 4 | `IsModernApp` | `0x22B00` | 10,140 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
