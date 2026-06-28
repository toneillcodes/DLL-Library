# Binary Specification: mssip32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mssip32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8c71160a0039e55aedf566465882076060d74989ba8b67a9b808ef0f2ac574cd`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CryptSIPCreateIndirectData` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPCreateIndirectData` |
| 1 | `CryptSIPGetInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPGetInfo` |
| 2 | `CryptSIPGetRegWorkingFlags` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPGetRegWorkingFlags` |
| 4 | `CryptSIPGetSignedDataMsg` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPGetSignedDataMsg` |
| 5 | `CryptSIPPutSignedDataMsg` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPPutSignedDataMsg` |
| 6 | `CryptSIPRemoveSignedDataMsg` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPRemoveSignedDataMsg` |
| 7 | `CryptSIPVerifyIndirectData` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptSIPVerifyIndirectData` |
| 8 | `DllRegisterServer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.mssip32DllRegisterServer` |
| 9 | `DllUnregisterServer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.mssip32DllUnregisterServer` |
