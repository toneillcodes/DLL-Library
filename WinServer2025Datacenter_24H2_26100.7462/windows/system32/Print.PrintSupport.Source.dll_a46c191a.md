# Binary Specification: Print.PrintSupport.Source.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Print.PrintSupport.Source.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a46c191af3eeb3bf1f54731f9d843113b1444cdea1d33dc3bb2ece5654635cf6`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `DllCanUnloadNow` | `0x8380` | 60 | UnwindData |  |
| 7 | `CreateSoftwareDevnode` | `0x2F070` | 542 | UnwindData |  |
| 9 | `DoesPsaHavePdcUpdatePolicyForPrinter` | `0x2F2A0` | 241 | UnwindData |  |
| 10 | `ExcludePdcRegenerationForPsaActivationProcess` | `0x2F3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetAppUserModelId` | `0x2F3B0` | 439 | UnwindData |  |
| 12 | `GetDeviceContainerIdByPerUserPrinterName` | `0x2F570` | 625 | UnwindData |  |
| 13 | `GetDeviceContainerIdByPrinterName` | `0x2F7F0` | 280 | UnwindData |  |
| 14 | `GetEntryPoint` | `0x2F910` | 462 | UnwindData |  |
| 15 | `GetSidFromUPPrinterName` | `0x2FAF0` | 124 | UnwindData |  |
| 18 | `HasAppWithContract` | `0x2FB80` | 662 | UnwindData |  |
| 19 | `IsActivationContractSupported` | `0x2FE20` | 322 | UnwindData |  |
| 20 | `IsActivationContractSupportedForUserContext` | `0x2FF70` | 1,228 | UnwindData |  |
| 21 | `IsCurrentProcessExcludedForPdcRegeneration` | `0x30450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `IsIppPrinterPsaEnabledForContractAsCurrentUser` | `0x30460` | 63 | UnwindData |  |
| 23 | `IsMandatoryPsaMissing` | `0x304B0` | 781 | UnwindData |  |
| 24 | `IsPdcRegneratedForPrinterWithAppByPrinterName` | `0x307D0` | 293 | UnwindData |  |
| 25 | `IsPrinterConnection` | `0x30900` | 704 | UnwindData |  |
| 26 | `IsPsaContractActivatableForDevice` | `0x30BD0` | 1,245 | UnwindData |  |
| 27 | `IsPsaEnabledForContract` | `0x310C0` | 861 | UnwindData |  |
| 28 | `IsPsaEnabledForContractAsCurrentUser` | `0x31430` | 63 | UnwindData |  |
| 29 | `IsPsaPreferredPdlConversionProcess` | `0x31480` | 54 | UnwindData |  |
| 30 | `IsSameUserContextBySid` | `0x314C0` | 246 | UnwindData |  |
| 32 | `LaunchSystemSettingsBroker` | `0x315C0` | 687 | UnwindData |  |
| 33 | `NotifyPsaOnCommunicationError` | `0x31880` | 812 | UnwindData |  |
| 35 | `OnPrinterSelected` | `0x31BC0` | 2,824 | UnwindData |  |
| 36 | `QueryAndSubscribePdmPrinterChangeNotification` | `0x326D0` | 439 | UnwindData |  |
| 37 | `RegeneratePdcForApp` | `0x32890` | 360 | UnwindData |  |
| 42 | `SetPsaPreferredPdlConversionProcess` | `0x32A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ShoudPdcBeUpdatedNow` | `0x32A10` | 190 | UnwindData |  |
| 44 | `UpdatePDC` | `0x32AE0` | 78 | UnwindData |  |
| 45 | `UpdatePDCAndPDR` | `0x32B40` | 2,610 | UnwindData |  |
| 46 | `UpdatePdcRegenerationRegKey` | `0x33580` | 675 | UnwindData |  |
| 1 | `CreateAndStartPsaSession` | `0x4A790` | 119 | UnwindData |  |
| 2 | `CreateAndStartPsaVirtualPrinterSession` | `0x4A810` | 928 | UnwindData |  |
| 3 | `CreatePsaManagerForUserContextAbi` | `0x4ABC0` | 212 | UnwindData |  |
| 4 | `CreatePsaPreferredPdlSourceStream` | `0x4ACA0` | 136 | UnwindData |  |
| 5 | `CreatePsaSessionForUserContext` | `0x4AD30` | 1,019 | UnwindData |  |
| 6 | `CreatePsaSourceStream` | `0x4B140` | 136 | UnwindData |  |
| 16 | `GetVirtualPrinterTargetFilePathForJob` | `0x4B1D0` | 317 | UnwindData |  |
| 17 | `GetVirtualPrinterTargetFileToken` | `0x4B320` | 210 | UnwindData |  |
| 31 | `LaunchPsaAppForError` | `0x4B400` | 184 | UnwindData |  |
| 34 | `NotifyPsaOnJobIssue` | `0x4B4C0` | 318 | UnwindData |  |
| 38 | `RemovePsaSession` | `0x4B610` | 54 | UnwindData |  |
| 39 | `RemovePsaSessionForUserContext` | `0x4B650` | 215 | UnwindData |  |
| 40 | `SetJobIdForPsaSession` | `0x4B730` | 216 | UnwindData |  |
| 41 | `SetPrintTicketPsa` | `0x4B810` | 606 | UnwindData |  |
| 47 | `ValidatePrintTicket` | `0x4BA80` | 997 | UnwindData |  |
| 48 | `ValidatePrintTicketAndGetShowsJobUI` | `0x4BE70` | 906 | UnwindData |  |
| 49 | `WaitForSetJobPrintTicketCompletion` | `0x4C200` | 332 | UnwindData |  |
