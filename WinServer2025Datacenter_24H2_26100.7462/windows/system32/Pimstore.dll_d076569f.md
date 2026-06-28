# Binary Specification: Pimstore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Pimstore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d076569fbcaa84386dbc4d3128d5cc49021f04bb3e892800243831f4ec4fbb07`
* **Total Exported Functions:** 89

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CopyCEPROPVAL` | `0x4670` | 43 | UnwindData |  |
| 89 | `TextToTag` | `0x4940` | 468 | UnwindData |  |
| 23 | `FindAllMatchingAggregates` | `0xE600` | 1,061 | UnwindData |  |
| 40 | `GetDefaultStoreItemId` | `0xFDB0` | 557 | UnwindData |  |
| 70 | `POutlookAppManager_CreateInstance` | `0xFFF0` | 324 | UnwindData |  |
| 42 | `GetDisplayBy` | `0x27C70` | 394 | UnwindData |  |
| 52 | `GetSortBy` | `0x27F10` | 398 | UnwindData |  |
| 35 | `GetContactDisplayAndSortPropertiesFromRegistry` | `0x28A90` | 247 | UnwindData |  |
| 30 | `GetAggregateCache` | `0x28C70` | 330 | UnwindData |  |
| 31 | `GetAggregateCacheGeneration` | `0x2E930` | 188 | UnwindData |  |
| 53 | `GetStartAndEndDate` | `0x37920` | 488 | UnwindData |  |
| 19 | `DllGetClassObject` | `0x39220` | 334 | UnwindData |  |
| 65 | `IsEmptyProp` | `0x3ED80` | 166 | UnwindData |  |
| 63 | `HasSameStoreFilter` | `0x421E0` | 106 | UnwindData |  |
| 38 | `GetDefaultStoreFilter` | `0x440D0` | 343 | UnwindData |  |
| 72 | `PimBinaryBodyToString` | `0x459B0` | 127 | UnwindData |  |
| 46 | `GetHighestUSStoreBit` | `0x48280` | 201 | UnwindData |  |
| 18 | `DllCanUnloadNow` | `0x4B320` | 68 | UnwindData |  |
| 36 | `GetDefaultFolderFromStore` | `0x4C010` | 64 | UnwindData |  |
| 37 | `GetDefaultFolderFromStoreEx` | `0x4C060` | 1,051 | UnwindData |  |
| 67 | `OlDefaultFoldersToOlItemType` | `0x4CAE0` | 87 | UnwindData |  |
| 11 | `CreateContactSettingsRegKey` | `0x4FDA0` | 949 | UnwindData |  |
| 9 | `CreateAttendeeList` | `0x50280` | 118 | UnwindData |  |
| 24 | `FindAllMatchingContactsEx` | `0x50AF0` | 157 | UnwindData |  |
| 5 | `CanonicalizedComparePropVal` | `0x52A60` | 764 | UnwindData |  |
| 39 | `GetDefaultStoreId` | `0x53A70` | 84 | UnwindData |  |
| 26 | `FindAllMatchingContactsEx3` | `0x53FD0` | 172 | UnwindData |  |
| 34 | `GetBlankName` | `0x541E0` | 13,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `HasAllBlobBitsSet` | `0x57580` | 207 | UnwindData |  |
| 1 | `?Submit@AccountProviderHostJobBase@@QEAAJPEAK@Z` | `0x5E210` | 142 | UnwindData |  |
| 2 | `?SubmitSynchronously@AccountProviderHostJobBase@@QEAAJPEAXKPEAT_SNJobOutParams@@@Z` | `0x5E2B0` | 744 | UnwindData |  |
| 3 | `BuildDisplayName` | `0x61640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BuildYomiDisplayName` | `0x61650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DestroyNameParser` | `0x61660` | 20 | UnwindData |  |
| 44 | `GetFullName` | `0x61680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `GetGivenName` | `0x616A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `GetMiddle` | `0x616D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GetNewNameParser` | `0x616F0` | 226 | UnwindData |  |
| 50 | `GetNickname` | `0x617E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `GetSuffix` | `0x61800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `GetSurname` | `0x61820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `GetTitle` | `0x61850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `GetYomiDisplayName` | `0x61870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetYomiGivenName` | `0x61890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `GetYomiSurname` | `0x618B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ParseName` | `0x618D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `RebuildName` | `0x618E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SetFullName` | `0x618F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `SetGiven` | `0x61910` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SetMiddle` | `0x61940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `SetNickname` | `0x61960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SetSuffix` | `0x61980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SetSurname` | `0x619A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `SetTitle` | `0x619D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `SetYomiGiven` | `0x619F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SetYomiSurname` | `0x61A10` | 8,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ClearPreferenceAndOverride` | `0x63CA0` | 469 | UnwindData |  |
| 29 | `GetActiveOutlookApp` | `0x63E80` | 371 | UnwindData |  |
| 43 | `GetFloatingTime` | `0x64000` | 649 | UnwindData |  |
| 69 | `OlObjectTypeFromOLITEMID` | `0x64340` | 218 | UnwindData |  |
| 75 | `SendPictureUpdateNotification` | `0x646F0` | 317 | UnwindData |  |
| 76 | `SetDisplayBy` | `0x64840` | 134 | UnwindData |  |
| 79 | `SetIncludeMiddle` | `0x648D0` | 169 | UnwindData |  |
| 82 | `SetSortBy` | `0x64980` | 134 | UnwindData |  |
| 7 | `CompareEmailAddresses` | `0x64B60` | 338 | UnwindData |  |
| 10 | `CreateCategoryDBManager` | `0x67990` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CreateItemInDefaultFolder` | `0x67B20` | 201 | UnwindData |  |
| 16 | `DisableLocalPoom` | `0x67BF0` | 25 | UnwindData |  |
| 17 | `DisableLocalPoomEx` | `0x67C10` | 56 | UnwindData |  |
| 20 | `EnableLocalPoom` | `0x67C50` | 66 | UnwindData |  |
| 21 | `EnableLocalPoomEx` | `0x67CA0` | 211 | UnwindData |  |
| 64 | `IsDefaultStore` | `0x67E40` | 150 | UnwindData |  |
| 13 | `CreateOutlookApp` | `0x6A460` | 154 | UnwindData |  |
| 88 | `StopNotifications` | `0x6A500` | 158 | UnwindData |  |
| 14 | `CreateRecurrenceFromData` | `0x6BCE0` | 174 | UnwindData |  |
| 22 | `EscapePoomRestrictionValues` | `0x6BF50` | 247 | UnwindData |  |
| 25 | `FindAllMatchingContactsEx2` | `0x74A50` | 70 | UnwindData |  |
| 27 | `FindMatchingContactEx` | `0x74AA0` | 41 | UnwindData |  |
| 28 | `FindMatchingContactEx2` | `0x74AD0` | 596 | UnwindData |  |
| 32 | `GetAppointmentFromUniqueId` | `0x76480` | 369 | UnwindData |  |
| 33 | `GetAppointmentUniqueId` | `0x76600` | 484 | UnwindData |  |
| 47 | `GetMeetingNotificationFromMessage` | `0x767F0` | 110 | UnwindData |  |
| 60 | `HandleMeetingResponseForAppointment` | `0x76870` | 480 | UnwindData |  |
| 61 | `HandleMeetingResponseForMeetingNotification` | `0x76A60` | 650 | UnwindData |  |
| 66 | `IsFEString` | `0x77540` | 112 | UnwindData |  |
| 41 | `GetDefaultUSStore` | `0x7AC60` | 139 | UnwindData |  |
| 51 | `GetPartnerGUID` | `0x7AD00` | 232 | UnwindData |  |
| 73 | `PimCreateGlobalObjId` | `0x7CCD0` | 193 | UnwindData |  |
| 68 | `OlItemTypeToOlDefaultFolders` | `0x7CF20` | 87 | UnwindData |  |
