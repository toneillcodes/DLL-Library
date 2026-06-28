# Binary Specification: nvui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ecda72b90f24107213bad159869c8d47f90c773ae23e20b0fbc44b21891bb1ff`
* **Total Exported Functions:** 83

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `?IsRunning@NotificationIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x68930` | 44 | UnwindData |  |
| 25 | `?UpdateTrayIcon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NPEB_W_N1@Z` | `0x68BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?UpdateTrayIconEx@NotificationIcon@UI@UXDriver@Nvidia@@SA_NPEB_WH_N1@Z` | `0x68C00` | 955 | UnwindData |  |
| 1 | `?Delete@NotificationIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x690A0` | 286 | UnwindData |  |
| 3 | `?IsAvailable@NotificationIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x69330` | 79 | UnwindData |  |
| 22 | `?StartNotificationIcon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NW4LoadPluginOption@234@W4QuitOption@234@W4EventFlag@234@@Z` | `0x69380` | 1,193 | UnwindData |  |
| 9 | `?Refresh@NotificationIcon@UI@UXDriver@Nvidia@@SAXXZ` | `0x69830` | 49 | UnwindData |  |
| 7 | `?IsThemedMessageWindowOpen@NotificationIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x69910` | 41 | UnwindData |  |
| 19 | `?ShowThemedMessageWindow@NotificationIcon@UI@UXDriver@Nvidia@@SA_NIIKPEAUHICON__@@PEB_W@Z` | `0x69940` | 282 | UnwindData |  |
| 20 | `?ShowThemedMessageWindow@NotificationIcon@UI@UXDriver@Nvidia@@SA_NPEB_W0KPEAUHICON__@@0@Z` | `0x69A60` | 725 | UnwindData |  |
| 18 | `?ShowThemedBalloon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NPEB_W0KPEAUHICON__@@0@Z` | `0x69D40` | 462 | UnwindData |  |
| 17 | `?ShowBalloonVariadic@NotificationIcon@UI@UXDriver@Nvidia@@SA_NIIIIIPEB_W000W4ExeType@234@ZZ` | `0x69F10` | 92 | UnwindData |  |
| 16 | `?ShowBalloonVariadic@NotificationIcon@UI@UXDriver@Nvidia@@SA_NIIIIIPEB_W000W4ExeType@234@PEAD@Z` | `0x69F70` | 2,241 | UnwindData |  |
| 15 | `?ShowBalloon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NPEB_W0KPEAUHICON__@@001W4ExeType@234@@Z` | `0x6A840` | 348 | UnwindData |  |
| 14 | `?ShowBalloon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NPEB_W0I0000@Z` | `0x6A9A0` | 248 | UnwindData |  |
| 13 | `?ShowBalloon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NIIPEAUHICON__@@PEB_W11@Z` | `0x6AAA0` | 402 | UnwindData |  |
| 11 | `?ShowBalloon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NIIIPEB_W000@Z` | `0x6AC40` | 441 | UnwindData |  |
| 12 | `?ShowBalloon@NotificationIcon@UI@UXDriver@Nvidia@@SA_NIIKPEB_W00@Z` | `0x6AE00` | 402 | UnwindData |  |
| 44 | `InitilizeResourceHandle` | `0x75BF0` | 30 | UnwindData |  |
| 33 | `DisplayTooltipWithoutExecuteW` | `0x75C10` | 185 | UnwindData |  |
| 32 | `DisplayTooltipWithExecuteW` | `0x75CD0` | 185 | UnwindData |  |
| 48 | `SelectRegion` | `0x75D90` | 41 | UnwindData |  |
| 30 | `CloseCloneToFitUI` | `0x75DC0` | 74 | UnwindData |  |
| 66 | `ShowSLIBlockingAppsDlg` | `0x75E10` | 255 | UnwindData |  |
| 56 | `ShowAceMUXBlockingAppsDlg` | `0x75F10` | 177 | UnwindData |  |
| 65 | `ShowPowerNotification` | `0x75FD0` | 240 | UnwindData |  |
| 70 | `ShowVideoBridgeNotification` | `0x760C0` | 282 | UnwindData |  |
| 67 | `ShowSurroundNotification` | `0x761E0` | 294 | UnwindData |  |
| 51 | `Show3DProfileInfo` | `0x76310` | 241 | UnwindData |  |
| 52 | `Show3DProfileInfoW` | `0x76410` | 182 | UnwindData |  |
| 79 | `StopNotificationIconW` | `0x764D0` | 104 | UnwindData |  |
| 81 | `StopXGpuTrayIconW` | `0x76540` | 104 | UnwindData |  |
| 80 | `StopXGpuTrayIcon` | `0x765B0` | 70 | UnwindData |  |
| 74 | `StartOptimusXGpuTrayIcon` | `0x76600` | 71 | UnwindData |  |
| 75 | `StartOptimusXGpuTrayIconUI` | `0x76650` | 63 | UnwindData |  |
| 71 | `StartACETrayIcon` | `0x76690` | 348 | UnwindData |  |
| 53 | `ShowACETrayIcon` | `0x767F0` | 67 | UnwindData |  |
| 43 | `HideACETrayIcon` | `0x76840` | 67 | UnwindData |  |
| 54 | `ShowAceDialog` | `0x76890` | 63 | UnwindData |  |
| 55 | `ShowAceDialogAsync` | `0x768D0` | 351 | UnwindData |  |
| 73 | `StartNotificationIcon` | `0x76A30` | 78 | UnwindData |  |
| 78 | `StopNotificationIcon` | `0x76A80` | 101 | UnwindData |  |
| 72 | `StartDx11SampleApp` | `0x76AF0` | 648 | UnwindData |  |
| 77 | `StopDx11SampleApp` | `0x76D80` | 87 | UnwindData |  |
| 45 | `IsNotificationIconAvailable` | `0x76DE0` | 34 | UnwindData |  |
| 46 | `IsNotificationIconRunning` | `0x76E10` | 34 | UnwindData |  |
| 42 | `GetWFDSyncHandle` | `0x76E40` | 37 | UnwindData |  |
| 64 | `ShowHCloneHotplugDialog` | `0x76E70` | 573 | UnwindData |  |
| 57 | `ShowBalloon` | `0x770B0` | 86 | UnwindData |  |
| 59 | `ShowBalloonVer1` | `0x77110` | 122 | UnwindData |  |
| 60 | `ShowBalloonVer2` | `0x77190` | 86 | UnwindData |  |
| 61 | `ShowBalloonVer3` | `0x771F0` | 86 | UnwindData |  |
| 62 | `ShowBalloonVer4` | `0x77250` | 90 | UnwindData |  |
| 63 | `ShowBalloonVer5` | `0x772B0` | 90 | UnwindData |  |
| 58 | `ShowBalloonVariadic` | `0x77310` | 151 | UnwindData |  |
| 29 | `ACEShowBalloonVariadic` | `0x773B0` | 151 | UnwindData |  |
| 68 | `ShowThemedBalloon` | `0x77450` | 90 | UnwindData |  |
| 69 | `ShowThemedMessageWindow` | `0x774B0` | 90 | UnwindData |  |
| 47 | `IsThemedMessageWindowOpen` | `0x77510` | 34 | UnwindData |  |
| 82 | `UpdateTrayIcon` | `0x77540` | 90 | UnwindData |  |
| 83 | `UpdateTrayIconEx` | `0x775A0` | 88 | UnwindData |  |
| 50 | `SetNotToRefreshTray` | `0x77600` | 55 | UnwindData |  |
| 76 | `StartWFDNotificationIcon` | `0x77640` | 34 | UnwindData |  |
| 41 | `GetLicenseServerDetails` | `0x77670` | 162 | UnwindData |  |
| 49 | `SetLicenseServerDetails` | `0x77720` | 387 | UnwindData |  |
| 39 | `EnableLicenseFeature` | `0x778B0` | 286 | UnwindData |  |
| 31 | `DisableLicenseFeature` | `0x779D0` | 286 | UnwindData |  |
| 40 | `GetLicensableFeatures` | `0x77AF0` | 101 | UnwindData |  |
| 34 | `DllCanUnloadNow` | `0x77CC0` | 66 | UnwindData |  |
| 35 | `DllGetClassObject` | `0x77D10` | 328 | UnwindData |  |
| 37 | `DllRegisterServer` | `0x77E60` | 297 | UnwindData |  |
| 38 | `DllUnregisterServer` | `0x77F90` | 277 | UnwindData |  |
| 36 | `DllInstall` | `0x780B0` | 97 | UnwindData |  |
| 6 | `?IsRunning@OptimusIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x78BE0` | 44 | UnwindData |  |
| 24 | `?StartOptimusUI@OptimusIcon@UI@UXDriver@Nvidia@@SAXXZ` | `0x78E90` | 37 | UnwindData |  |
| 26 | `?UpdateTrayIcon@OptimusIcon@UI@UXDriver@Nvidia@@SA_NPEB_W_N1@Z` | `0x78EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?UpdateTrayIconEx@OptimusIcon@UI@UXDriver@Nvidia@@SA_NPEB_WH_N1@Z` | `0x78EE0` | 823 | UnwindData |  |
| 2 | `?Delete@OptimusIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x79310` | 331 | UnwindData |  |
| 4 | `?IsAvailable@OptimusIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x79460` | 59 | UnwindData |  |
| 23 | `?StartOptimusIcon@OptimusIcon@UI@UXDriver@Nvidia@@SAXW4LoadPluginOption@234@W4QuitOption@234@W4EventFlag@234@@Z` | `0x794A0` | 1,286 | UnwindData |  |
| 10 | `?Refresh@OptimusIcon@UI@UXDriver@Nvidia@@SAXXZ` | `0x799B0` | 49 | UnwindData |  |
| 8 | `?IsThemedMessageWindowOpen@OptimusIcon@UI@UXDriver@Nvidia@@SA_NXZ` | `0x799F0` | 41 | UnwindData |  |
| 21 | `?ShowThemedMessageWindow@OptimusIcon@UI@UXDriver@Nvidia@@SA_NPEB_W0KPEAUHICON__@@0@Z` | `0x79A20` | 708 | UnwindData |  |
