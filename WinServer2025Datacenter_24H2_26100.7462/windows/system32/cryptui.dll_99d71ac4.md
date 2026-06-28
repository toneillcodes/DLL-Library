# Binary Specification: cryptui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `99d71ac4dd06ae4742fb617b7a7d3e1b381198de27d916ddc52e453b31a32082`
* **Total Exported Functions:** 56

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `CryptDllProtectPrompt` | `0x4180` | 161 | UnwindData |  |
| 4 | `CompareCertificate` | `0x8D00` | 380 | UnwindData |  |
| 35 | `CryptUIDlgViewContext` | `0xB6D0` | 240 | UnwindData |  |
| 10 | `GetUnknownErrorString` | `0x144C0` | 200 | UnwindData |  |
| 47 | `CryptUIViewExpiringCerts` | `0x181B0` | 163 | UnwindData |  |
| 9 | `FormatDateStringAutoLayout` | `0x1AE30` | 393 | UnwindData |  |
| 12 | `MyFormatEnhancedKeyUsageString` | `0x1D700` | 88 | UnwindData |  |
| 2 | `CertDllLogMismatchPinRules` | `0x21B10` | 637 | UnwindData |  |
| 17 | `CryptUIDlgCertMgr` | `0x252C0` | 493 | UnwindData |  |
| 46 | `CryptUIStartCertMgr` | `0x254C0` | 50 | UnwindData |  |
| 5 | `CryptUIDlgAddPolicyServer` | `0x267A0` | 105 | UnwindData |  |
| 6 | `CryptUIDlgAddPolicyServerWithPriority` | `0x26810` | 378 | UnwindData |  |
| 7 | `CryptUIDlgPropertyPolicy` | `0x26990` | 294 | UnwindData |  |
| 32 | `CryptUIDlgViewCertificatePropertiesA` | `0x2E5D0` | 185 | UnwindData |  |
| 33 | `CryptUIDlgViewCertificatePropertiesW` | `0x2E690` | 866 | UnwindData |  |
| 38 | `CryptUIFreeCertificatePropertiesPagesA` | `0x2EA00` | 27 | UnwindData |  |
| 39 | `CryptUIFreeCertificatePropertiesPagesW` | `0x2EA00` | 27 | UnwindData |  |
| 40 | `CryptUIFreeViewSignaturesPagesA` | `0x2EA00` | 27 | UnwindData |  |
| 41 | `CryptUIFreeViewSignaturesPagesW` | `0x2EA00` | 27 | UnwindData |  |
| 42 | `CryptUIGetCertificatePropertiesPagesA` | `0x2EA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CryptUIGetCertificatePropertiesPagesW` | `0x2EA40` | 632 | UnwindData |  |
| 3 | `CertDllProtectedRootMessageBox` | `0x2ECC0` | 511 | UnwindData |  |
| 18 | `CryptUIDlgFreeCAContext` | `0x30120` | 81 | UnwindData |  |
| 19 | `CryptUIDlgFreePolicyServerContext` | `0x30180` | 102 | UnwindData |  |
| 20 | `CryptUIDlgSelectCA` | `0x301F0` | 1,986 | UnwindData |  |
| 24 | `CryptUIDlgSelectPolicyServer` | `0x309C0` | 660 | UnwindData |  |
| 25 | `CryptUIDlgSelectStoreA` | `0x33920` | 147 | UnwindData |  |
| 26 | `CryptUIDlgSelectStoreW` | `0x339C0` | 166 | UnwindData |  |
| 1 | `AddChainToStore` | `0x36BD0` | 473 | UnwindData |  |
| 8 | `DisplayHtmlHelp` | `0x37000` | 135 | UnwindData |  |
| 11 | `InvokeHelpLink` | `0x37960` | 160 | UnwindData |  |
| 15 | `CommonInit` | `0x38190` | 41 | UnwindData |  |
| 54 | `DllRegisterServer` | `0x381C0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `DllUnregisterServer` | `0x381C0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `CryptUIDlgViewCRLA` | `0x38440` | 143 | UnwindData |  |
| 28 | `CryptUIDlgViewCRLW` | `0x384E0` | 655 | UnwindData |  |
| 29 | `CryptUIDlgViewCTLA` | `0x38780` | 165 | UnwindData |  |
| 30 | `CryptUIDlgViewCTLW` | `0x38830` | 789 | UnwindData |  |
| 31 | `CryptUIDlgViewCertificateA` | `0x38B50` | 198 | UnwindData |  |
| 34 | `CryptUIDlgViewCertificateW` | `0x38C20` | 1,536 | UnwindData |  |
| 36 | `CryptUIDlgViewSignerInfoA` | `0x39230` | 163 | UnwindData |  |
| 37 | `CryptUIDlgViewSignerInfoW` | `0x397B0` | 42 | UnwindData |  |
| 44 | `CryptUIGetViewSignaturesPagesA` | `0x3C8C0` | 182 | UnwindData |  |
| 45 | `CryptUIGetViewSignaturesPagesW` | `0x3C980` | 663 | UnwindData |  |
| 48 | `CryptUIWizBuildCTL` | `0x3D2C0` | 191 | UnwindData |  |
| 49 | `CryptUIWizDigitalSign` | `0x3D390` | 178 | UnwindData |  |
| 50 | `CryptUIWizExport` | `0x3D450` | 226 | UnwindData |  |
| 51 | `CryptUIWizFreeDigitalSignContext` | `0x3D540` | 166 | UnwindData |  |
| 52 | `CryptUIWizImport` | `0x3D5F0` | 226 | UnwindData |  |
| 53 | `CryptUIWizImportInternal` | `0x3D6E0` | 226 | UnwindData |  |
| 56 | `IsWizardExtensionAvailable` | `0x3D7D0` | 56 | UnwindData |  |
| 14 | `CertSelectionGetSerializedBlob` | `0x3DD50` | 309 | UnwindData |  |
| 21 | `CryptUIDlgSelectCertificateA` | `0x3DE90` | 231 | UnwindData |  |
| 22 | `CryptUIDlgSelectCertificateFromStore` | `0x3DF80` | 163 | UnwindData |  |
| 23 | `CryptUIDlgSelectCertificateW` | `0x3E030` | 970 | UnwindData |  |
| 13 | `ACUIProviderInvokeUI` | `0x3FA80` | 293 | UnwindData |  |
