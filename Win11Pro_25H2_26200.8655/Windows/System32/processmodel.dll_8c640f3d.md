# Binary Specification: processmodel.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\processmodel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8c640f3de3272906f5cd9ab1a9510a51629dcbed6af7c1c3de39e873563023b1`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Experimental_CompileSandboxSpecificationInternal` | `0xE410` | 3,836 | UnwindData |  |
| 4 | `Experimental_FreeSandboxSpecification` | `0xF320` | 13,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `Experimental_CreateProcessAsUserInSandbox` | `0x12730` | 891 | UnwindData |  |
| 3 | `Experimental_CreateProcessInSandbox` | `0x12AC0` | 985 | UnwindData |  |
| 5 | `SbeCreateProcessAsUserInSandbox` | `0x16DB0` | 3,456 | UnwindData |  |
| 6 | `SbeCreateProcessAsUserInSandboxWithPolicyRulesEnforcement` | `0x17B40` | 735 | UnwindData |  |
