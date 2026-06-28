# Binary Specification: efswrt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\efswrt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8bcdb956b3688838d5adf5116c45036977e1aba2fb27151b31295ff9244ca561`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `DllCanUnloadNow` | `0xA620` | 58 | UnwindData |  |
| 14 | `DllGetActivationFactory` | `0xA660` | 45 | UnwindData |  |
| 15 | `DllGetClassObject` | `0xA6A0` | 134 | UnwindData |  |
| 1 | `CdplGetFileProtectionLevel` | `0x10D10` | 80 | UnwindData |  |
| 2 | `CdplGetFileProtectionLevelAndUser` | `0x10D70` | 79 | UnwindData |  |
| 3 | `CdplIsAppAllowedToRun` | `0x10DD0` | 2,789 | UnwindData |  |
| 4 | `CdplIsAppDataProtectionSupported` | `0x118C0` | 48,545 | UnwindData |  |
| 5 | `CdplIsSupported` | `0x1D670` | 57 | UnwindData |  |
| 6 | `CdplProtectFileToLevel` | `0x1D6B0` | 304 | UnwindData |  |
| 7 | `CdplProtectFileToLevelWithResult` | `0x1D7F0` | 288 | UnwindData |  |
| 8 | `CdplProtectKnownUserFolders` | `0x1D920` | 713 | UnwindData |  |
| 9 | `CdplProtectSecretToLevel` | `0x1DBF0` | 192 | UnwindData |  |
| 10 | `CdplSetIsPolicyEnabledForCurrentUser` | `0x1DCC0` | 322 | UnwindData |  |
| 11 | `CdplSetIsPolicyEnabledForUser` | `0x1DE10` | 400 | UnwindData |  |
| 12 | `CdplUnprotectSecret` | `0x1DFB0` | 23 | UnwindData |  |
| 16 | `DpmBufferFree` | `0x1DFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `DpmProtectSecretToIdentity` | `0x1DFE0` | 334 | UnwindData |  |
| 18 | `DpmStreamClose` | `0x1E140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `DpmStreamOpenToProtectToIdentity` | `0x1E150` | 233 | UnwindData |  |
| 20 | `DpmStreamOpenToUnprotect` | `0x1E240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `DpmStreamUpdate` | `0x1E250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DpmUnprotectSecret` | `0x1E260` | 99 | UnwindData |  |
| 23 | `EnterpriseDataCopyProtection` | `0x1E2D0` | 716 | UnwindData |  |
| 24 | `EnterpriseDataGetStatus` | `0x1E5B0` | 692 | UnwindData |  |
| 25 | `EnterpriseDataProtect` | `0x1E870` | 810 | UnwindData |  |
| 26 | `EnterpriseDataRevoke` | `0x1EBA0` | 1,017 | UnwindData |  |
| 27 | `FreeIdentityProtectorList` | `0x1EFA0` | 27 | UnwindData |  |
| 28 | `GetEnterpriseActionForCopy` | `0x1EFD0` | 1,404 | UnwindData |  |
| 29 | `GetEnterpriseIdForNetworkPath` | `0x1F560` | 235 | UnwindData |  |
| 30 | `ProtectFileToEnterpriseIdentity` | `0x1F660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ProtectFileToIdentity` | `0x1F680` | 365 | UnwindData |  |
| 32 | `ProtectOrReprotectFileToIdentity` | `0x1F800` | 220 | UnwindData |  |
| 33 | `QueryIdentityProtectors` | `0x1F8F0` | 437 | UnwindData |  |
| 34 | `UnprotectFile` | `0x1FAB0` | 344,659 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
