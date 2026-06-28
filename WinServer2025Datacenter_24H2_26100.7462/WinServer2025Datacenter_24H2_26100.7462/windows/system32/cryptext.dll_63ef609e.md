# Binary Specification: cryptext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `63ef609ed5b1d7575ac62acc5628bd362b4106b8f2c78beba0eccb1b3e11e224`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 32 | `DllCanUnloadNow` | `0x28F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DllGetClassObject` | `0x2910` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DllRegisterServer` | `0x2A10` | 102 | UnwindData |  |
| 35 | `DllUnregisterServer` | `0x2A80` | 64 | UnwindData |  |
| 1 | `I_InvokeCommand` | `0x32C0` | 902 | UnwindData |  |
| 2 | `CryptExtAddCER` | `0x6440` | 132 | UnwindData |  |
| 3 | `CryptExtAddCERMachineOnlyAndHwndW` | `0x64D0` | 456 | UnwindData |  |
| 4 | `CryptExtAddCERW` | `0x66A0` | 277 | UnwindData |  |
| 5 | `CryptExtAddCRL` | `0x67C0` | 132 | UnwindData |  |
| 6 | `CryptExtAddCRLW` | `0x6850` | 274 | UnwindData |  |
| 7 | `CryptExtAddCTL` | `0x6970` | 132 | UnwindData |  |
| 8 | `CryptExtAddCTLW` | `0x6A00` | 274 | UnwindData |  |
| 9 | `CryptExtAddP7R` | `0x6B20` | 120 | UnwindData |  |
| 10 | `CryptExtAddP7RW` | `0x6BA0` | 738 | UnwindData |  |
| 11 | `CryptExtAddPFX` | `0x6E90` | 132 | UnwindData |  |
| 12 | `CryptExtAddPFXMachineOnlyAndHwndW` | `0x6F20` | 342 | UnwindData |  |
| 13 | `CryptExtAddPFXW` | `0x7080` | 221 | UnwindData |  |
| 14 | `CryptExtAddSPC` | `0x7170` | 132 | UnwindData |  |
| 15 | `CryptExtAddSPCW` | `0x7200` | 240 | UnwindData |  |
| 16 | `CryptExtOpenCAT` | `0x7300` | 132 | UnwindData |  |
| 17 | `CryptExtOpenCATW` | `0x7390` | 217 | UnwindData |  |
| 18 | `CryptExtOpenCER` | `0x7470` | 134 | UnwindData |  |
| 19 | `CryptExtOpenCERW` | `0x7500` | 254 | UnwindData |  |
| 20 | `CryptExtOpenCRL` | `0x7610` | 132 | UnwindData |  |
| 21 | `CryptExtOpenCRLW` | `0x76A0` | 251 | UnwindData |  |
| 22 | `CryptExtOpenCTL` | `0x77B0` | 132 | UnwindData |  |
| 23 | `CryptExtOpenCTLW` | `0x7840` | 200 | UnwindData |  |
| 24 | `CryptExtOpenP7R` | `0x7910` | 120 | UnwindData |  |
| 25 | `CryptExtOpenP7RW` | `0x7990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `CryptExtOpenPFX` | `0x79A0` | 132 | UnwindData |  |
| 27 | `CryptExtOpenPFXW` | `0x7A30` | 160 | UnwindData |  |
| 28 | `CryptExtOpenPKCS7` | `0x7AE0` | 132 | UnwindData |  |
| 29 | `CryptExtOpenPKCS7W` | `0x7B70` | 237 | UnwindData |  |
| 30 | `CryptExtOpenSTR` | `0x7C70` | 132 | UnwindData |  |
| 31 | `CryptExtOpenSTRW` | `0x7D00` | 201 | UnwindData |  |
