# Binary Specification: Print.PrintSupport.Source.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Print.PrintSupport.Source.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b1a8866099f66058e5f1edbc06b7b4710742eedc53716363b3dd227a9c9c8889`
* **Total Exported Functions:** 50

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `DllCanUnloadNow` | `0x81D0` | 60 | UnwindData |  |
| 7 | `CreateSoftwareDevnode` | `0x2C510` | 542 | UnwindData |  |
| 9 | `DoesPsaHavePdcUpdatePolicyForPrinter` | `0x2C740` | 190 | UnwindData |  |
| 10 | `ExcludePdcRegenerationForPsaActivationProcess` | `0x2C810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetAppUserModelId` | `0x2C820` | 346 | UnwindData |  |
| 12 | `GetDeviceContainerIdByPerUserPrinterName` | `0x2C980` | 264 | UnwindData |  |
| 13 | `GetDeviceContainerIdByPrinterName` | `0x2CA90` | 280 | UnwindData |  |
| 14 | `GetEntryPoint` | `0x2CBB0` | 462 | UnwindData |  |
| 15 | `GetSidFromUPPrinterName` | `0x2CD90` | 124 | UnwindData |  |
| 18 | `HasAppWithContract` | `0x2CE20` | 533 | UnwindData |  |
| 19 | `IsActivationContractSupported` | `0x2D040` | 322 | UnwindData |  |
| 20 | `IsActivationContractSupportedForUserContext` | `0x2D190` | 1,228 | UnwindData |  |
| 21 | `IsCurrentProcessExcludedForPdcRegeneration` | `0x2D670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `IsIppPrinterPsaEnabledForContractAsCurrentUser` | `0x2D680` | 63 | UnwindData |  |
| 23 | `IsMandatoryPsaMissing` | `0x2D6D0` | 719 | UnwindData |  |
| 24 | `IsPdcRegneratedForPrinterWithAppByPrinterName` | `0x2D9B0` | 293 | UnwindData |  |
| 25 | `IsPrinterConnection` | `0x2DAE0` | 36 | UnwindData |  |
| 26 | `IsPsaContractActivatableForDevice` | `0x2DB10` | 1,229 | UnwindData |  |
| 27 | `IsPsaEnabledForContract` | `0x2DFF0` | 693 | UnwindData |  |
| 28 | `IsPsaEnabledForContractAsCurrentUser` | `0x2E2B0` | 63 | UnwindData |  |
| 29 | `IsPsaPreferredPdlConversionProcess` | `0x2E300` | 54 | UnwindData |  |
| 30 | `IsSameUserContextBySid` | `0x2E340` | 246 | UnwindData |  |
| 32 | `LaunchSystemSettingsBroker` | `0x2E440` | 687 | UnwindData |  |
| 33 | `NotifyPsaOnCommunicationError` | `0x2E700` | 46 | UnwindData |  |
| 35 | `OnPrinterSelected` | `0x2E740` | 2,824 | UnwindData |  |
| 36 | `QueryAndSubscribePdmPrinterChangeNotification` | `0x2F250` | 439 | UnwindData |  |
| 37 | `RegeneratePdcForApp` | `0x2F410` | 360 | UnwindData |  |
| 43 | `SetPsaPreferredPdlConversionProcess` | `0x2F580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ShoudPdcBeUpdatedNow` | `0x2F590` | 190 | UnwindData |  |
| 45 | `UpdatePDC` | `0x2F660` | 78 | UnwindData |  |
| 46 | `UpdatePDCAndPDR` | `0x2F6C0` | 3,033 | UnwindData |  |
| 47 | `UpdatePdcRegenerationRegKey` | `0x302A0` | 675 | UnwindData |  |
| 1 | `CreateAndStartPsaSession` | `0x399E0` | 119 | UnwindData |  |
| 2 | `CreateAndStartPsaVirtualPrinterSession` | `0x39A60` | 826 | UnwindData |  |
| 3 | `CreatePsaManagerForUserContextAbi` | `0x39DA0` | 212 | UnwindData |  |
| 4 | `CreatePsaPreferredPdlSourceStream` | `0x39E80` | 136 | UnwindData |  |
| 5 | `CreatePsaSessionForUserContext` | `0x39F10` | 934 | UnwindData |  |
| 6 | `CreatePsaSourceStream` | `0x3A2C0` | 136 | UnwindData |  |
| 16 | `GetVirtualPrinterTargetFilePathForJob` | `0x3A350` | 317 | UnwindData |  |
| 17 | `GetVirtualPrinterTargetFileToken` | `0x3A4A0` | 210 | UnwindData |  |
| 31 | `LaunchPsaAppForError` | `0x3A580` | 184 | UnwindData |  |
| 34 | `NotifyPsaOnJobIssue` | `0x3A640` | 318 | UnwindData |  |
| 38 | `RemovePsaSession` | `0x3A790` | 54 | UnwindData |  |
| 39 | `RemovePsaSessionForUserContext` | `0x3A7D0` | 215 | UnwindData |  |
| 40 | `SetJobIdForPsaSession` | `0x3A8B0` | 216 | UnwindData |  |
| 41 | `SetPassthroughJobAndOperationAttributes` | `0x3A990` | 549 | UnwindData |  |
| 42 | `SetPrintTicketPsa` | `0x3ABC0` | 365 | UnwindData |  |
| 48 | `ValidatePrintTicket` | `0x3AD40` | 866 | UnwindData |  |
| 49 | `ValidatePrintTicketAndGetShowsJobUI` | `0x3B0B0` | 906 | UnwindData |  |
| 50 | `WaitForSetJobPrintTicketCompletion` | `0x3B440` | 332 | UnwindData |  |
