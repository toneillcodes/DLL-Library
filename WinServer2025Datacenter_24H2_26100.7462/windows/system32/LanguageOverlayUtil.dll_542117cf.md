# Binary Specification: LanguageOverlayUtil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\LanguageOverlayUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `542117cf6dda8e032c2e0c9b05fb61fe28355688b1edae76a433883a16329e0f`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `GetOverlayFilePath` | `0x81F0` | 25 | UnwindData |  |
| 1 | `LogonTaskTelemetryInfoInit` | `0x8C10` | 16,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `EnumerateSupportedUILanguages` | `0xCD50` | 154 | UnwindData |  |
| 2 | `OnMachineUILanguageInit` | `0x141A0` | 128 | UnwindData |  |
| 3 | `OnMachineUILanguageSwitch` | `0x14230` | 155 | UnwindData |  |
| 4 | `AddLanguageToMachineLanguageList` | `0x18FD0` | 431 | UnwindData |  |
| 5 | `DeleteLanguageInstallationRequest` | `0x19190` | 293 | UnwindData |  |
| 6 | `DeleteLanguageInstallationState` | `0x192C0` | 307 | UnwindData |  |
| 7 | `EnumerateInstalledLanguageFeatures` | `0x19400` | 886 | UnwindData |  |
| 8 | `EnumerateInstalledLanguages` | `0x19780` | 492 | UnwindData |  |
| 9 | `EnumerateInstalledLocalExperiencePacks` | `0x19980` | 111 | UnwindData |  |
| 10 | `EnumerateInstalledSystemLanguagePacks` | `0x19A00` | 58 | UnwindData |  |
| 11 | `EnumerateLocalExperiencePacksForExpeditedUpdate` | `0x19A40` | 827 | UnwindData |  |
| 12 | `EnumerateOverlayPaths` | `0x19D90` | 280 | UnwindData |  |
| 13 | `EnumerateQueuedLanguageInstallations` | `0x19EB0` | 198 | UnwindData |  |
| 15 | `FetchLanguageOverlayPackageForFirstLogon` | `0x19F80` | 738 | UnwindData |  |
| 16 | `GetBcp47TagFromPackageFamilyName` | `0x1A270` | 1,345 | UnwindData |  |
| 17 | `GetInstalledLanguagePackType` | `0x1A7C0` | 163 | UnwindData |  |
| 18 | `GetLanguageDataForLogging` | `0x1A870` | 754 | UnwindData |  |
| 19 | `GetLanguageInstallationState` | `0x1AB70` | 696 | UnwindData |  |
| 20 | `GetLanguageOverlayPackageFamilyName` | `0x1AE30` | 1,034 | UnwindData |  |
| 21 | `GetLanguagesInUse` | `0x1B240` | 511 | UnwindData |  |
| 23 | `GetOverlayPriMergeChecksum` | `0x1B450` | 690 | UnwindData |  |
| 24 | `GetSystemPreferredUILanguage` | `0x1B710` | 858 | UnwindData |  |
| 26 | `GetWindowsUpdateServer` | `0x1BA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `GroupUserLanguages` | `0x1BA80` | 251 | UnwindData |  |
| 29 | `InvalidateLanguageResourceCaches` | `0x1BB90` | 328 | UnwindData |  |
| 30 | `IsGroupingUserLanguagesNeeded` | `0x1BCE0` | 264 | UnwindData |  |
| 31 | `IsLocalExperiencePackReadyForRemoval` | `0x1BDF0` | 116 | UnwindData |  |
| 32 | `OverlaySetPreferredUILanguages` | `0x1BE70` | 722 | UnwindData |  |
| 33 | `RemoveLanguageFromMachineLanguageList` | `0x1C150` | 411 | UnwindData |  |
| 34 | `ResetOverlayPriMergeChecksum` | `0x1C300` | 296 | UnwindData |  |
| 35 | `SetLanguageInstallationState` | `0x1C430` | 338 | UnwindData |  |
| 36 | `SetSystemPreferredUILanguage` | `0x1C590` | 716 | UnwindData |  |
| 37 | `ShouldInstallOverlayPackageDuringLogonForLanguage` | `0x1C870` | 101 | UnwindData |  |
| 38 | `StartLanguageInstallation` | `0x1C8E0` | 745 | UnwindData |  |
| 39 | `StartLanguageUninstallation` | `0x1CBD0` | 293 | UnwindData |  |
| 25 | `GetUnusedLanguagesToCleanup` | `0x1DD60` | 334 | UnwindData |  |
| 28 | `HandleUnusedLanguagesCleanupResult` | `0x1DEC0` | 203 | UnwindData |  |
