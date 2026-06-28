# Binary Specification: softpub.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\softpub.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a2b18dcaa0fee7dbe3e5fba6cedbfff65f8da74f841a7b819411d295ad4b99b`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `AddPersonalTrustDBPages` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.AddPersonalTrustDBPages` |
| 8 | `DllRegisterServer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubDllRegisterServer` |
| 9 | `DllUnregisterServer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubDllUnregisterServer` |
| 10 | `DriverCleanupPolicy` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.DriverCleanupPolicy` |
| 11 | `DriverFinalPolicy` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.DriverFinalPolicy` |
| 12 | `DriverInitializePolicy` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.DriverInitializePolicy` |
| 13 | `FindCertsByIssuer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.FindCertsByIssuer` |
| 1 | `GenericChainCertificateTrust` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.GenericChainCertificateTrust` |
| 2 | `GenericChainFinalProv` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.GenericChainFinalProv` |
| 3 | `HTTPSCertificateTrust` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.HTTPSCertificateTrust` |
| 14 | `HTTPSFinalProv` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.HTTPSFinalProv` |
| 15 | `OfficeCleanupPolicy` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.OfficeCleanupPolicy` |
| 16 | `OfficeInitializePolicy` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.OfficeInitializePolicy` |
| 17 | `OpenPersonalTrustDBDialog` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.OpenPersonalTrustDBDialog` |
| 18 | `SoftpubAuthenticode` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubAuthenticode` |
| 19 | `SoftpubCheckCert` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubCheckCert` |
| 20 | `SoftpubCleanup` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubCleanup` |
| 4 | `SoftpubDefCertInit` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubDefCertInit` |
| 21 | `SoftpubDumpStructure` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubDumpStructure` |
| 5 | `SoftpubFreeDefUsageCallData` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubFreeDefUsageCallData` |
| 22 | `SoftpubInitialize` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubInitialize` |
| 6 | `SoftpubLoadDefUsageCallData` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubLoadDefUsageCallData` |
| 23 | `SoftpubLoadMessage` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubLoadMessage` |
| 24 | `SoftpubLoadSignature` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.SoftpubLoadSignature` |
