# Binary Specification: printui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\printui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `790d176f38d74ae5d6859a1b4d7c23236154c5da1da57ee312bbb92f16cc315a`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllMain` | `0x5770` | 47 | UnwindData |  |
| 41 | *Ordinal Only* | `0x6070` | 252 | UnwindData |  |
| 1 | `ConstructPrinterFriendlyName` | `0x9FE0` | 45,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `bFolderEnumPrinters` | `0x152E0` | 29,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `bFolderGetPrinter` | `0x152E0` | 29,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `bFolderRefresh` | `0x152E0` | 29,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `vServerPropPages` | `0x1C6F0` | 158 | UnwindData |  |
| 27 | `vDocumentDefaults` | `0x1D3D0` | 180 | UnwindData |  |
| 28 | `vPrinterPropPages` | `0x24430` | 178 | UnwindData |  |
| 2 | `PnPInterface` | `0x281D0` | 680 | UnwindData |  |
| 26 | `bPrinterSetup` | `0x34A20` | 105 | UnwindData |  |
| 8 | `DllCanUnloadNow` | `0x360B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllGetClassObject` | `0x360C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllRegisterServer` | `0x360D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllUnregisterServer` | `0x360D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `RegisterPrintNotify` | `0x360D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `UnregisterPrintNotify` | `0x360D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `vQueueCreate` | `0x36160` | 221 | UnwindData |  |
| 14 | `LaunchPlatformHelp` | `0x38E10` | 320 | UnwindData |  |
| 17 | `PrintUIDownloadAndInstallLegacyDriver` | `0x38F60` | 159 | UnwindData |  |
| 19 | `ShowErrorMessageHR` | `0x39010` | 280 | UnwindData |  |
| 20 | `ShowErrorMessageSC` | `0x39130` | 204 | UnwindData |  |
| 21 | `ShowHelpLinkDialog` | `0x39210` | 739 | UnwindData |  |
| 13 | `DocumentPropertiesWrap` | `0x3AB30` | 116 | UnwindData |  |
| 33 | `PrintUIEntryDPIAwareW` | `0x3F860` | 81 | UnwindData |  |
| 3 | `PrintUIEntryW` | `0x3F8C0` | 503 | UnwindData |  |
| 39 | *Ordinal Only* | `0x46150` | 123 | UnwindData |  |
| 40 | *Ordinal Only* | `0x46280` | 213 | UnwindData |  |
| 5 | `ReleaseArgv` | `0x494F0` | 79 | UnwindData |  |
| 6 | `StringToArgv` | `0x49550` | 569 | UnwindData |  |
| 4 | `PrinterPropPageProvider` | `0x4A9C0` | 94 | UnwindData |  |
| 7 | `ConnectToPrinterDlg` | `0x4D5A0` | 278 | UnwindData |  |
| 15 | `PrintNotifyTray_Exit` | `0x4F800` | 31 | UnwindData |  |
| 16 | `PrintNotifyTray_Init` | `0x4F830` | 31 | UnwindData |  |
