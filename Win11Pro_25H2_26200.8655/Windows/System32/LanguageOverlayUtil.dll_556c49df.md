# Binary Specification: LanguageOverlayUtil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\LanguageOverlayUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `556c49df788ca12becbb86b74332c3c505cc984713d07d4e4b6e53a05eae9f70`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `GetOverlayFilePath` | `0x8200` | 25 | UnwindData |  |
| 1 | `LogonTaskTelemetryInfoInit` | `0x8C20` | 16,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `EnumerateSupportedUILanguages` | `0xCD60` | 154 | UnwindData |  |
| 2 | `OnMachineUILanguageInit` | `0x141B0` | 128 | UnwindData |  |
| 3 | `OnMachineUILanguageSwitch` | `0x14240` | 155 | UnwindData |  |
| 4 | `AddLanguageToMachineLanguageList` | `0x18FE0` | 431 | UnwindData |  |
| 5 | `DeleteLanguageInstallationRequest` | `0x191A0` | 293 | UnwindData |  |
| 6 | `DeleteLanguageInstallationState` | `0x192D0` | 307 | UnwindData |  |
| 7 | `EnumerateInstalledLanguageFeatures` | `0x19410` | 886 | UnwindData |  |
| 8 | `EnumerateInstalledLanguages` | `0x19790` | 492 | UnwindData |  |
| 9 | `EnumerateInstalledLocalExperiencePacks` | `0x19990` | 111 | UnwindData |  |
| 10 | `EnumerateInstalledSystemLanguagePacks` | `0x19A10` | 58 | UnwindData |  |
| 11 | `EnumerateLocalExperiencePacksForExpeditedUpdate` | `0x19A50` | 827 | UnwindData |  |
| 12 | `EnumerateOverlayPaths` | `0x19DA0` | 280 | UnwindData |  |
| 13 | `EnumerateQueuedLanguageInstallations` | `0x19EC0` | 198 | UnwindData |  |
| 15 | `FetchLanguageOverlayPackageForFirstLogon` | `0x19F90` | 746 | UnwindData |  |
| 16 | `GetBcp47TagFromPackageFamilyName` | `0x1A280` | 1,345 | UnwindData |  |
| 17 | `GetInstalledLanguagePackType` | `0x1A7D0` | 163 | UnwindData |  |
| 18 | `GetLanguageDataForLogging` | `0x1A880` | 754 | UnwindData |  |
| 19 | `GetLanguageInstallationState` | `0x1AB80` | 696 | UnwindData |  |
| 20 | `GetLanguageOverlayPackageFamilyName` | `0x1AE40` | 1,034 | UnwindData |  |
| 21 | `GetLanguagesInUse` | `0x1B250` | 511 | UnwindData |  |
| 23 | `GetOverlayPriMergeChecksum` | `0x1B460` | 690 | UnwindData |  |
| 24 | `GetSystemPreferredUILanguage` | `0x1B720` | 858 | UnwindData |  |
| 26 | `GetWindowsUpdateServer` | `0x1BA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `GroupUserLanguages` | `0x1BA90` | 251 | UnwindData |  |
| 29 | `InvalidateLanguageResourceCaches` | `0x1BBA0` | 328 | UnwindData |  |
| 30 | `IsGroupingUserLanguagesNeeded` | `0x1BCF0` | 264 | UnwindData |  |
| 31 | `IsLocalExperiencePackReadyForRemoval` | `0x1BE00` | 116 | UnwindData |  |
| 32 | `OverlaySetPreferredUILanguages` | `0x1BE80` | 722 | UnwindData |  |
| 33 | `RemoveLanguageFromMachineLanguageList` | `0x1C160` | 411 | UnwindData |  |
| 34 | `ResetOverlayPriMergeChecksum` | `0x1C310` | 296 | UnwindData |  |
| 35 | `SetLanguageInstallationState` | `0x1C440` | 338 | UnwindData |  |
| 36 | `SetSystemPreferredUILanguage` | `0x1C5A0` | 716 | UnwindData |  |
| 37 | `ShouldInstallOverlayPackageDuringLogonForLanguage` | `0x1C880` | 101 | UnwindData |  |
| 38 | `StartLanguageInstallation` | `0x1C8F0` | 745 | UnwindData |  |
| 39 | `StartLanguageUninstallation` | `0x1CBE0` | 293 | UnwindData |  |
| 25 | `GetUnusedLanguagesToCleanup` | `0x1DD70` | 334 | UnwindData |  |
| 28 | `HandleUnusedLanguagesCleanupResult` | `0x1DED0` | 203 | UnwindData |  |
