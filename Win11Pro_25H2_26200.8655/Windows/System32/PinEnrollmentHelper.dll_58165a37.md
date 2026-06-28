# Binary Specification: PinEnrollmentHelper.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\PinEnrollmentHelper.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `58165a3782bcc3a56903f48fac561f37cc5ac202ad9d7b4507674f23f4a6c27f`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `GetProxyDllInfo` | `0x3A40` | 15,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x7740` | 75 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x77A0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x77E0` | 115 | UnwindData |  |
| 4 | `EnablePinForSignIn` | `0x78D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EnrollEnterpriseKey` | `0x78E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `EnrollPin` | `0x78F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `IsArsoAllowedByPolicy` | `0x7900` | 48 | UnwindData |  |
| 9 | `IsEnrollmentPermittedForLocalAccountWithoutPassword` | `0x7940` | 43,596 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
