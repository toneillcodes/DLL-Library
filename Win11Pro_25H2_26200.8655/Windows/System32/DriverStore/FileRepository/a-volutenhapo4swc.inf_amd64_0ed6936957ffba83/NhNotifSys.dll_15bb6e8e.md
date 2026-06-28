# Binary Specification: NhNotifSys.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\a-volutenhapo4swc.inf_amd64_0ed6936957ffba83\NhNotifSys.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15bb6e8eb6296050c739d2aa64d0f87f4ed61518e3249c9dce4167eef8e0c6a7`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Analytics_Create` | `0x2C860` | 342 | UnwindData |  |
| 2 | `Analytics_Destroy` | `0x2C9C0` | 49 | UnwindData |  |
| 7 | `Analytics_Start` | `0x2CB80` | 24 | UnwindData |  |
| 8 | `Analytics_Stop` | `0x2CBA0` | 24 | UnwindData |  |
| 5 | `Analytics_RegisterUWPAppTracking` | `0x2CBC0` | 353 | UnwindData |  |
| 4 | `Analytics_RegisterDriverTracking` | `0x2CD30` | 353 | UnwindData |  |
| 3 | `Analytics_RegisterAgsSettingsTracking` | `0x2CEA0` | 423 | UnwindData |  |
| 6 | `Analytics_RegisterVendorIdTracking` | `0x2D050` | 158 | UnwindData |  |
| 11 | `Analytics_TrackNotificationShown` | `0x2D0F0` | 140 | UnwindData |  |
| 10 | `Analytics_TrackNotificationDismissed` | `0x2D180` | 140 | UnwindData |  |
| 9 | `Analytics_TrackNotificationActivated` | `0x2D210` | 140 | UnwindData |  |
| 12 | `Analytics_TrackSettingChanged` | `0x2D2A0` | 423 | UnwindData |  |
| 13 | `Analytics_TrackUninstalled` | `0x2D450` | 24 | UnwindData |  |
| 14 | `AppUpdater_Create` | `0x2D470` | 306 | UnwindData |  |
| 19 | `DriverUpdater_Create` | `0x2D470` | 306 | UnwindData |  |
| 20 | `DriverUpdater_Destroy` | `0x2D5B0` | 172 | UnwindData |  |
| 22 | `DriverUpdater_GetUpdateVersion` | `0x2D660` | 577 | UnwindData |  |
| 21 | `DriverUpdater_Download` | `0x2D8B0` | 150 | UnwindData |  |
| 23 | `DriverUpdater_Update` | `0x2D950` | 150 | UnwindData |  |
| 24 | `Driver_GetVersion` | `0x2D9F0` | 670 | UnwindData |  |
| 15 | `AppUpdater_Destroy` | `0x2DC90` | 172 | UnwindData |  |
| 17 | `AppUpdater_GetUpdateVersion` | `0x2DD40` | 577 | UnwindData |  |
| 16 | `AppUpdater_Download` | `0x2DF90` | 244 | UnwindData |  |
| 18 | `AppUpdater_Update` | `0x2E090` | 150 | UnwindData |  |
| 25 | `PackageInfo_Create` | `0x2E130` | 41 | UnwindData |  |
| 26 | `PackageInfo_Destroy` | `0x2E160` | 56 | UnwindData |  |
| 27 | `PackageInfo_GetPackageVersion` | `0x2E1A0` | 667 | UnwindData |  |
| 28 | `PackageInfo_MonitorPackageInstallation` | `0x2E440` | 73 | UnwindData |  |
| 29 | `System_GetVendorIds` | `0x2E490` | 320 | UnwindData |  |
| 30 | `User_GetAnonymousId` | `0x2E5D0` | 202 | UnwindData |  |
