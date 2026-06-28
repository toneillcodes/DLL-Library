# Binary Specification: VsGraphicsProxyStub.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\VsGraphicsProxyStub.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dfa8036abbf3f3343b714e03b3a3afd3b0c62833f6e4a337db380aa21982cea0`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2330` | 53 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x23A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x23D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PixEngine_RegisterProxyStubClassObject` | `0x2400` | 120 | UnwindData |  |
| 6 | `PixEngine_RegisterProxyStubs` | `0x2480` | 1,233 | UnwindData |  |
| 7 | `PixEngine_UnregisterProxyStubClassObject` | `0x2960` | 0 | Indeterminate |  |
