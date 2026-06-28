# Binary Specification: edputil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\edputil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `99e847f9c46485ada94431f6573ab6df64342520606db3e20d730384b6e108e2`
* **Total Exported Functions:** 58

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `EdpGetContextForImpersonatedToken` | `0x2520` | 641 | UnwindData |  |
| 4 | `EdpCheckAccess` | `0x27B0` | 437 | UnwindData |  |
| 19 | `EdpGetContextForWindow` | `0x2990` | 1,122 | UnwindData |  |
| 18 | `EdpGetContextForProcess` | `0x2F70` | 1,287 | UnwindData |  |
| 27 | `EdpGetIsManaged` | `0x3480` | 386 | UnwindData |  |
| 25 | `EdpGetEnterpriseIdForUIEnforcementFromProcess` | `0x4110` | 416 | UnwindData |  |
| 10 | `EdpFreeContext` | `0x42C0` | 197 | UnwindData |  |
| 11 | `EdpGetAppLockerUniqueAppIdentifier` | `0x5290` | 701 | UnwindData |  |
| 13 | `EdpGetAppLockerUniqueAppIdentifierByTokenEx` | `0x63F0` | 463 | UnwindData |  |
| 38 | `EdpIsUIPolicyEvaluationEnabledForThread` | `0x7B50` | 29 | UnwindData |  |
| 39 | `EdpIsValidSubjectForEncryption` | `0x7CF0` | 103 | UnwindData |  |
| 20 | `EdpGetDataInfoFromDataObject` | `0x8F60` | 701 | UnwindData |  |
| 23 | `EdpGetEnterpriseIdForDataObject` | `0x9800` | 520 | UnwindData |  |
| 29 | `EdpGetPrimaryIdentities` | `0xA030` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `EdpShouldShowEnterpriseIndicator` | `0xA4E0` | 490 | UnwindData |  |
| 22 | `EdpGetEnterpriseIdForClipboard` | `0xA6D0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EdpCheckAccessForContext` | `0xAC20` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `EdpUtilFreeEnterpriseContext` | `0xAFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `EdpUtilIsAppEnlightened` | `0xAFF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EdpCanCallerAccessWin32Clipboard` | `0xB020` | 635 | UnwindData |  |
| 45 | `EdpSetEnterpriseIdForClipboard` | `0xBAC0` | 62 | UnwindData |  |
| 12 | `EdpGetAppLockerUniqueAppIdentifierByToken` | `0xC160` | 20 | UnwindData |  |
| 51 | `EdpUtilGetEnterpriseContextByName` | `0xC330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `EdpGetSourceIsEnlightenedForClipboard` | `0xC340` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `EdpIsFileAccessAllowed` | `0xC7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `EdpGetSourceAppIdForClipboard` | `0xC7B0` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `EdpGetEnterpriseIdForUIEnforcement` | `0xCD20` | 19,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `EdpAddAppClipboardConsentInCache` | `0x118A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EdpAuditAction` | `0x118B0` | 1,097 | UnwindData |  |
| 6 | `EdpCheckIsDpapiNgEntId` | `0x11D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EdpCheckIsRmsEntId` | `0x11D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `EdpClearClipboardMetaData` | `0x11D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EdpConvertProtectorToExternalId` | `0x11D30` | 25 | UnwindData |  |
| 28 | `EdpGetPersonalEnterpriseIdString` | `0x11D50` | 197 | UnwindData |  |
| 30 | `EdpGetPrimaryIdentityIfManaged` | `0x11E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `EdpGetRevocationInfo` | `0x11E40` | 60 | UnwindData |  |
| 34 | `EdpGetWindowFromThreadId` | `0x11E90` | 402 | UnwindData |  |
| 35 | `EdpIsAppClipboardConsentCached` | `0x12030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `EdpParseIdentityString` | `0x12040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `EdpParseProtectorDescriptor` | `0x12050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `EdpQueryIdentityWithProtectorDescriptor` | `0x12060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `EdpSetSourceAppIdForClipboard` | `0x12070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `EdpSetSourceIsEnlightenedForClipboard` | `0x12080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `EdpUtilCreateEnterpriseContextFromEnterpriseId` | `0x12090` | 270 | UnwindData |  |
| 52 | `EdpUtilGetEnterpriseContextByProcess` | `0x121B0` | 480 | UnwindData |  |
| 53 | `EdpUtilGetEnterpriseContextByWindowHandle` | `0x123A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `EdpUtilGetEnterpriseContextForView` | `0x123A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `EdpUtilGetEnterpriseContextForCurrentView` | `0x123B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `EdpUtilQueryPolicy` | `0x123C0` | 89 | UnwindData |  |
| 58 | `GetProcessUniqueIdFromToken` | `0x12420` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `EdpGetClipboardAccessDeniedData` | `0x12980` | 846 | UnwindData |  |
| 21 | `EdpGetDataInfoFromWin32Clipboard` | `0x12CE0` | 302 | UnwindData |  |
| 26 | `EdpGetFilePathsForDataObject` | `0x12E20` | 596 | UnwindData |  |
| 15 | `EdpGetContextForBinaryPath` | `0x13D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `EdpGetContextForPackageFullName` | `0x13D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `EdpIsContextExemptOrEnlightenedAllowed` | `0x13D60` | 305 | UnwindData |  |
| 43 | `EdpRequestAccess` | `0x13EA0` | 457 | UnwindData |  |
| 44 | `EdpRequestAccessForContext` | `0x14070` | 65 | UnwindData |  |
