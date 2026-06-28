# Binary Specification: cryptui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5f6f6b4a4a8cef6b9981d4338e708293139065428fad55a8f8c51c7f22ab2469`
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
| 12 | `MyFormatEnhancedKeyUsageString` | `0x1D720` | 88 | UnwindData |  |
| 2 | `CertDllLogMismatchPinRules` | `0x21B50` | 637 | UnwindData |  |
| 17 | `CryptUIDlgCertMgr` | `0x25300` | 493 | UnwindData |  |
| 46 | `CryptUIStartCertMgr` | `0x25500` | 50 | UnwindData |  |
| 5 | `CryptUIDlgAddPolicyServer` | `0x267E0` | 105 | UnwindData |  |
| 6 | `CryptUIDlgAddPolicyServerWithPriority` | `0x26850` | 378 | UnwindData |  |
| 7 | `CryptUIDlgPropertyPolicy` | `0x269D0` | 294 | UnwindData |  |
| 32 | `CryptUIDlgViewCertificatePropertiesA` | `0x2E610` | 185 | UnwindData |  |
| 33 | `CryptUIDlgViewCertificatePropertiesW` | `0x2E6D0` | 866 | UnwindData |  |
| 38 | `CryptUIFreeCertificatePropertiesPagesA` | `0x2EA40` | 27 | UnwindData |  |
| 39 | `CryptUIFreeCertificatePropertiesPagesW` | `0x2EA40` | 27 | UnwindData |  |
| 40 | `CryptUIFreeViewSignaturesPagesA` | `0x2EA40` | 27 | UnwindData |  |
| 41 | `CryptUIFreeViewSignaturesPagesW` | `0x2EA40` | 27 | UnwindData |  |
| 42 | `CryptUIGetCertificatePropertiesPagesA` | `0x2EA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CryptUIGetCertificatePropertiesPagesW` | `0x2EA80` | 632 | UnwindData |  |
| 3 | `CertDllProtectedRootMessageBox` | `0x2ED00` | 511 | UnwindData |  |
| 18 | `CryptUIDlgFreeCAContext` | `0x30160` | 81 | UnwindData |  |
| 19 | `CryptUIDlgFreePolicyServerContext` | `0x301C0` | 102 | UnwindData |  |
| 20 | `CryptUIDlgSelectCA` | `0x30230` | 1,986 | UnwindData |  |
| 24 | `CryptUIDlgSelectPolicyServer` | `0x30A00` | 660 | UnwindData |  |
| 25 | `CryptUIDlgSelectStoreA` | `0x33960` | 147 | UnwindData |  |
| 26 | `CryptUIDlgSelectStoreW` | `0x33A00` | 166 | UnwindData |  |
| 1 | `AddChainToStore` | `0x36C10` | 473 | UnwindData |  |
| 8 | `DisplayHtmlHelp` | `0x37040` | 135 | UnwindData |  |
| 11 | `InvokeHelpLink` | `0x379A0` | 160 | UnwindData |  |
| 15 | `CommonInit` | `0x381D0` | 41 | UnwindData |  |
| 54 | `DllRegisterServer` | `0x38200` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `DllUnregisterServer` | `0x38200` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `CryptUIDlgViewCRLA` | `0x38480` | 143 | UnwindData |  |
| 28 | `CryptUIDlgViewCRLW` | `0x38520` | 655 | UnwindData |  |
| 29 | `CryptUIDlgViewCTLA` | `0x387C0` | 165 | UnwindData |  |
| 30 | `CryptUIDlgViewCTLW` | `0x38870` | 789 | UnwindData |  |
| 31 | `CryptUIDlgViewCertificateA` | `0x38B90` | 198 | UnwindData |  |
| 34 | `CryptUIDlgViewCertificateW` | `0x38C60` | 1,536 | UnwindData |  |
| 36 | `CryptUIDlgViewSignerInfoA` | `0x39270` | 163 | UnwindData |  |
| 37 | `CryptUIDlgViewSignerInfoW` | `0x397F0` | 42 | UnwindData |  |
| 44 | `CryptUIGetViewSignaturesPagesA` | `0x3C900` | 182 | UnwindData |  |
| 45 | `CryptUIGetViewSignaturesPagesW` | `0x3C9C0` | 663 | UnwindData |  |
| 48 | `CryptUIWizBuildCTL` | `0x3D300` | 191 | UnwindData |  |
| 49 | `CryptUIWizDigitalSign` | `0x3D3D0` | 178 | UnwindData |  |
| 50 | `CryptUIWizExport` | `0x3D490` | 226 | UnwindData |  |
| 51 | `CryptUIWizFreeDigitalSignContext` | `0x3D580` | 166 | UnwindData |  |
| 52 | `CryptUIWizImport` | `0x3D630` | 226 | UnwindData |  |
| 53 | `CryptUIWizImportInternal` | `0x3D720` | 226 | UnwindData |  |
| 56 | `IsWizardExtensionAvailable` | `0x3D810` | 56 | UnwindData |  |
| 14 | `CertSelectionGetSerializedBlob` | `0x3DD90` | 309 | UnwindData |  |
| 21 | `CryptUIDlgSelectCertificateA` | `0x3DED0` | 231 | UnwindData |  |
| 22 | `CryptUIDlgSelectCertificateFromStore` | `0x3DFC0` | 163 | UnwindData |  |
| 23 | `CryptUIDlgSelectCertificateW` | `0x3E070` | 970 | UnwindData |  |
| 13 | `ACUIProviderInvokeUI` | `0x3FAC0` | 293 | UnwindData |  |
