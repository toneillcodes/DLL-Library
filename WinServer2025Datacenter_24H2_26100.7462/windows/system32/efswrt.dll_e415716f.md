# Binary Specification: efswrt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\efswrt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e415716faef1648e785023bc93d8885f8ff753b1c5f38e07a2d06d5dfbe4dc28`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `DllCanUnloadNow` | `0xA620` | 58 | UnwindData |  |
| 14 | `DllGetActivationFactory` | `0xA660` | 45 | UnwindData |  |
| 15 | `DllGetClassObject` | `0xA6A0` | 134 | UnwindData |  |
| 1 | `CdplGetFileProtectionLevel` | `0x10CE0` | 80 | UnwindData |  |
| 2 | `CdplGetFileProtectionLevelAndUser` | `0x10D40` | 79 | UnwindData |  |
| 3 | `CdplIsAppAllowedToRun` | `0x10DA0` | 2,785 | UnwindData |  |
| 4 | `CdplIsAppDataProtectionSupported` | `0x11890` | 48,545 | UnwindData |  |
| 5 | `CdplIsSupported` | `0x1D640` | 57 | UnwindData |  |
| 6 | `CdplProtectFileToLevel` | `0x1D680` | 304 | UnwindData |  |
| 7 | `CdplProtectFileToLevelWithResult` | `0x1D7C0` | 288 | UnwindData |  |
| 8 | `CdplProtectKnownUserFolders` | `0x1D8F0` | 713 | UnwindData |  |
| 9 | `CdplProtectSecretToLevel` | `0x1DBC0` | 192 | UnwindData |  |
| 10 | `CdplSetIsPolicyEnabledForCurrentUser` | `0x1DC90` | 322 | UnwindData |  |
| 11 | `CdplSetIsPolicyEnabledForUser` | `0x1DDE0` | 400 | UnwindData |  |
| 12 | `CdplUnprotectSecret` | `0x1DF80` | 23 | UnwindData |  |
| 16 | `DpmBufferFree` | `0x1DFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `DpmProtectSecretToIdentity` | `0x1DFB0` | 334 | UnwindData |  |
| 18 | `DpmStreamClose` | `0x1E110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `DpmStreamOpenToProtectToIdentity` | `0x1E120` | 233 | UnwindData |  |
| 20 | `DpmStreamOpenToUnprotect` | `0x1E210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `DpmStreamUpdate` | `0x1E220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DpmUnprotectSecret` | `0x1E230` | 99 | UnwindData |  |
| 23 | `EnterpriseDataCopyProtection` | `0x1E2A0` | 716 | UnwindData |  |
| 24 | `EnterpriseDataGetStatus` | `0x1E580` | 692 | UnwindData |  |
| 25 | `EnterpriseDataProtect` | `0x1E840` | 810 | UnwindData |  |
| 26 | `EnterpriseDataRevoke` | `0x1EB70` | 1,017 | UnwindData |  |
| 27 | `FreeIdentityProtectorList` | `0x1EF70` | 27 | UnwindData |  |
| 28 | `GetEnterpriseActionForCopy` | `0x1EFA0` | 1,404 | UnwindData |  |
| 29 | `GetEnterpriseIdForNetworkPath` | `0x1F530` | 235 | UnwindData |  |
| 30 | `ProtectFileToEnterpriseIdentity` | `0x1F630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ProtectFileToIdentity` | `0x1F650` | 365 | UnwindData |  |
| 32 | `ProtectOrReprotectFileToIdentity` | `0x1F7D0` | 220 | UnwindData |  |
| 33 | `QueryIdentityProtectors` | `0x1F8C0` | 437 | UnwindData |  |
| 34 | `UnprotectFile` | `0x1FA80` | 343,955 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
