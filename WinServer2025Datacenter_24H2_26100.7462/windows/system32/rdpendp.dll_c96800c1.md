# Binary Specification: rdpendp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rdpendp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c96800c181061184183316571a89d389409d883f883df8dfcf3bc908c2e9258f`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x29B0` | 157 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x2A60` | 394 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2EB0` | 131,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x2EB0` | 131,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetTSAudioEndpointEnumeratorForSession` | `0x23050` | 668 | UnwindData |  |
