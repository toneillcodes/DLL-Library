# Binary Specification: printui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\printui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `05368b211cbe48973af6a7d9bf404261c59c132faf70efd79dee93bcf772996a`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllMain` | `0x5750` | 47 | UnwindData |  |
| 41 | *Ordinal Only* | `0x6050` | 252 | UnwindData |  |
| 1 | `ConstructPrinterFriendlyName` | `0x9FF0` | 45,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `bFolderEnumPrinters` | `0x151C0` | 29,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `bFolderGetPrinter` | `0x151C0` | 29,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `bFolderRefresh` | `0x151C0` | 29,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `vServerPropPages` | `0x1C5D0` | 158 | UnwindData |  |
| 27 | `vDocumentDefaults` | `0x1D2B0` | 180 | UnwindData |  |
| 28 | `vPrinterPropPages` | `0x24310` | 178 | UnwindData |  |
| 2 | `PnPInterface` | `0x28520` | 680 | UnwindData |  |
| 26 | `bPrinterSetup` | `0x351E0` | 105 | UnwindData |  |
| 8 | `DllCanUnloadNow` | `0x36C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllGetClassObject` | `0x36C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x36C80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllUnregisterServer` | `0x36C80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `RegisterPrintNotify` | `0x36C80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `UnregisterPrintNotify` | `0x36C80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `vQueueCreate` | `0x36D10` | 221 | UnwindData |  |
| 14 | `LaunchPlatformHelp` | `0x399C0` | 320 | UnwindData |  |
| 17 | `PrintUIDownloadAndInstallLegacyDriver` | `0x39B10` | 159 | UnwindData |  |
| 19 | `ShowErrorMessageHR` | `0x39BC0` | 280 | UnwindData |  |
| 20 | `ShowErrorMessageSC` | `0x39CE0` | 204 | UnwindData |  |
| 21 | `ShowHelpLinkDialog` | `0x39DC0` | 739 | UnwindData |  |
| 13 | `DocumentPropertiesWrap` | `0x3B6E0` | 116 | UnwindData |  |
| 33 | `PrintUIEntryDPIAwareW` | `0x40410` | 81 | UnwindData |  |
| 3 | `PrintUIEntryW` | `0x40470` | 503 | UnwindData |  |
| 39 | *Ordinal Only* | `0x46D00` | 123 | UnwindData |  |
| 40 | *Ordinal Only* | `0x46E30` | 213 | UnwindData |  |
| 5 | `ReleaseArgv` | `0x4A0A0` | 79 | UnwindData |  |
| 6 | `StringToArgv` | `0x4A100` | 569 | UnwindData |  |
| 4 | `PrinterPropPageProvider` | `0x4B4A0` | 94 | UnwindData |  |
| 7 | `ConnectToPrinterDlg` | `0x4D9A0` | 278 | UnwindData |  |
| 15 | `PrintNotifyTray_Exit` | `0x4FC00` | 31 | UnwindData |  |
| 16 | `PrintNotifyTray_Init` | `0x4FC30` | 31 | UnwindData |  |
