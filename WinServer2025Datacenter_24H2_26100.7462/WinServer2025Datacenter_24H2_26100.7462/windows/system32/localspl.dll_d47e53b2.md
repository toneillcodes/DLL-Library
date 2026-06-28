# Binary Specification: localspl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\localspl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d47e53b217c5fae0771b71de5a60d9ec45f57dd43020e30fcdf584b5d70fa3c4`
* **Total Exported Functions:** 124

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 469 | `SplEnumPorts` | `0x125E0` | 172 | UnwindData |  |
| 504 | `SplOpenPrinter` | `0x14570` | 151 | UnwindData |  |
| 477 | `SplEnumPrinters` | `0x151C0` | 256 | UnwindData |  |
| 517 | `SplSetPrinterDataEx` | `0x25FB0` | 257 | UnwindData |  |
| 523 | `SplXcvData` | `0x2B030` | 188 | UnwindData |  |
| 475 | `SplEnumPrinterDrivers` | `0x2D1F0` | 174 | UnwindData |  |
| 490 | `SplGetPrinterDriverDirectory` | `0x31620` | 154 | UnwindData |  |
| 482 | `SplGetPrintClassObject` | `0x31B80` | 56 | UnwindData |  |
| 483 | `SplGetPrintClassObject_4CSR` | `0x31BC0` | 140 | UnwindData |  |
| 451 | `SplDeleteMonitor` | `0x34600` | 142 | UnwindData |  |
| 494 | `SplGetUserPropertyBag` | `0x3E210` | 111 | UnwindData |  |
| 442 | `SplClosePrinter` | `0x3F820` | 88 | UnwindData |  |
| 515 | `SplSetPrinter` | `0x40390` | 145 | UnwindData |  |
| 486 | `SplGetPrinter` | `0x41290` | 149 | UnwindData |  |
| 467 | `SplEnumJobs` | `0x43FB0` | 173 | UnwindData |  |
| 480 | `SplGetJob` | `0x44070` | 157 | UnwindData |  |
| 512 | `SplSetJob` | `0x44120` | 149 | UnwindData |  |
| 429 | `LocalReadPrinter` | `0x44ED0` | 142 | UnwindData |  |
| 522 | `SplWritePrinter` | `0x45B70` | 142 | UnwindData |  |
| 407 | `SplGetDriverUpdateStatus` | `0x47920` | 154 | UnwindData |  |
| 491 | `SplGetPrinterDriverEx` | `0x49910` | 123 | UnwindData |  |
| 463 | `SplDriverEvent` | `0x4AA90` | 141 | UnwindData |  |
| 421 | `DllMain` | `0x4E770` | 792 | UnwindData |  |
| 448 | `SplCreateSpooler` | `0x4F870` | 126 | UnwindData |  |
| 456 | `SplDeletePrinterData` | `0x51D80` | 174 | UnwindData |  |
| 457 | `SplDeletePrinterDataEx` | `0x51E40` | 183 | UnwindData |  |
| 474 | `SplEnumPrinterDataEx` | `0x51F00` | 155 | UnwindData |  |
| 487 | `SplGetPrinterData` | `0x51FB0` | 248 | UnwindData |  |
| 488 | `SplGetPrinterDataEx` | `0x520B0` | 166 | UnwindData |  |
| 516 | `SplSetPrinterData` | `0x52160` | 252 | UnwindData |  |
| 466 | `SplEnumForms` | `0x53210` | 157 | UnwindData |  |
| 424 | `InitializePrintMonitor2` | `0x66EC0` | 574 | UnwindData |  |
| 505 | `SplPlayGdiScriptOnPrinterIC` | `0x689A0` | 85 | UnwindData |  |
| 403 | `SplAddCSRPrinter` | `0x800E0` | 161 | UnwindData |  |
| 404 | `SplDoesCSRPrinterDevnodeExist` | `0x80190` | 155 | UnwindData |  |
| 405 | `SplEnableCSRPrinterDeviceInterface` | `0x80240` | 227 | UnwindData |  |
| 412 | `SplIsValidUserPropertyBag` | `0x80330` | 113 | UnwindData |  |
| 440 | `SplAddPrinter` | `0x81E70` | 166 | UnwindData |  |
| 455 | `SplDeletePrinter` | `0x81F20` | 202 | UnwindData |  |
| 461 | `SplDeletePrinterWithJobs` | `0x81FF0` | 129 | UnwindData |  |
| 507 | `SplRegeneratePrintDeviceCapabilities` | `0x82080` | 99 | UnwindData |  |
| 509 | `SplResetPrinter` | `0x820F0` | 122 | UnwindData |  |
| 409 | `SplGetLocalDevMode` | `0x83340` | 215 | UnwindData |  |
| 413 | `SplNotifyServerStatus` | `0x85830` | 237 | UnwindData |  |
| 415 | `SplSetCSRPrinterDevnode` | `0x85930` | 111 | UnwindData |  |
| 492 | `SplGetPrinterExtra` | `0x859B0` | 122 | UnwindData |  |
| 493 | `SplGetPrinterExtraEx` | `0x85A30` | 122 | UnwindData |  |
| 518 | `SplSetPrinterExtra` | `0x85AB0` | 122 | UnwindData |  |
| 519 | `SplSetPrinterExtraEx` | `0x85B30` | 122 | UnwindData |  |
| 408 | `SplGetJobExtra` | `0x8AED0` | 268 | UnwindData |  |
| 417 | `SplSetJobError` | `0x8AFF0` | 408 | UnwindData |  |
| 418 | `SplSetJobExtra` | `0x8B190` | 238 | UnwindData |  |
| 450 | `SplDeleteJobNamedProperty` | `0x8BCE0` | 123 | UnwindData |  |
| 481 | `SplGetJobNamedPropertyValue` | `0x8BD70` | 135 | UnwindData |  |
| 513 | `SplSetJobNamedProperty` | `0x8BE00` | 123 | UnwindData |  |
| 401 | `LclIsSessionZero` | `0x8C0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `LclPromptUIPerSessionUser` | `0x8C0C0` | 141 | UnwindData |  |
| 433 | `SplAbortPrinter` | `0x905A0` | 110 | UnwindData |  |
| 464 | `SplEndDocPrinter` | `0x90620` | 220 | UnwindData |  |
| 465 | `SplEndPagePrinter` | `0x90710` | 110 | UnwindData |  |
| 520 | `SplStartDocPrinter` | `0x90880` | 233 | UnwindData |  |
| 521 | `SplStartPagePrinter` | `0x90970` | 110 | UnwindData |  |
| 435 | `SplAddJob` | `0x91A80` | 149 | UnwindData |  |
| 510 | `SplScheduleJob` | `0x91B20` | 122 | UnwindData |  |
| 410 | `SplIsDriverInstalled` | `0x967B0` | 129 | UnwindData |  |
| 411 | `SplIsLocalDriverAvailable` | `0x96840` | 129 | UnwindData |  |
| 416 | `SplSetDriverUpdateStatus` | `0x968D0` | 411 | UnwindData |  |
| 441 | `SplAddPrinterDriverEx` | `0x98E40` | 158 | UnwindData |  |
| 458 | `SplDeletePrinterDriverEx` | `0x98EF0` | 162 | UnwindData |  |
| 489 | `SplGetPrinterDriver` | `0x98FA0` | 67 | UnwindData |  |
| 501 | `SplIsCompatibleDriver` | `0x98FF0` | 147 | UnwindData |  |
| 478 | `SplGetDriverDir` | `0x9B8A0` | 130 | UnwindData |  |
| 400 | *Ordinal Only* | `0x9B930` | 112 | UnwindData |  |
| 503 | `SplMonitorIsInstalled` | `0x9B9B0` | 110 | UnwindData |  |
| 425 | `InitializePrintProvidor` | `0xA15D0` | 118 | UnwindData |  |
| 443 | `SplCloseSpooler` | `0xA2660` | 110 | UnwindData |  |
| 462 | `SplDeleteSpooler` | `0xA29C0` | 110 | UnwindData |  |
| 460 | `SplDeletePrinterKey` | `0xAEAD0` | 115 | UnwindData |  |
| 473 | `SplEnumPrinterData` | `0xAEB50` | 188 | UnwindData |  |
| 476 | `SplEnumPrinterKey` | `0xAEC20` | 147 | UnwindData |  |
| 414 | `SplReenumeratePorts` | `0xB0990` | 42 | UnwindData |  |
| 436 | `SplAddMonitor` | `0xB1020` | 141 | UnwindData |  |
| 437 | `SplAddPort` | `0xB10C0` | 142 | UnwindData |  |
| 438 | `SplAddPortEx` | `0xB1160` | 149 | UnwindData |  |
| 452 | `SplDeletePort` | `0xB1410` | 142 | UnwindData |  |
| 468 | `SplEnumMonitors` | `0xB14B0` | 165 | UnwindData |  |
| 419 | `ClosePrintProcessor` | `0xB3D70` | 110 | UnwindData |  |
| 420 | `ControlPrintProcessor` | `0xB3DF0` | 122 | UnwindData |  |
| 422 | `EnumPrintProcessorDatatypesW` | `0xB3E70` | 166 | UnwindData |  |
| 423 | `GetPrintProcessorCapabilities` | `0xB3F20` | 146 | UnwindData |  |
| 431 | `OpenPrintProcessor` | `0xB3FC0` | 124 | UnwindData |  |
| 432 | `PrintDocumentOnPrintProcessor` | `0xB4050` | 122 | UnwindData |  |
| 439 | `SplAddPrintProcessor` | `0xB40D0` | 143 | UnwindData |  |
| 453 | `SplDeletePrintProcCacheData` | `0xB4170` | 112 | UnwindData |  |
| 454 | `SplDeletePrintProcessor` | `0xB41F0` | 142 | UnwindData |  |
| 470 | `SplEnumPrintProcCacheData` | `0xB4290` | 127 | UnwindData |  |
| 471 | `SplEnumPrintProcessorDatatypes` | `0xB4320` | 174 | UnwindData |  |
| 472 | `SplEnumPrintProcessors` | `0xB43E0` | 174 | UnwindData |  |
| 484 | `SplGetPrintProcCacheData` | `0xB44A0` | 147 | UnwindData |  |
| 485 | `SplGetPrintProcessorDirectory` | `0xB4540` | 157 | UnwindData |  |
| 514 | `SplSetPrintProcCacheData` | `0xB45F0` | 139 | UnwindData |  |
| 426 | `LocalAddForm` | `0xB6AC0` | 141 | UnwindData |  |
| 427 | `LocalDeleteForm` | `0xB6B60` | 122 | UnwindData |  |
| 428 | `LocalEnumForms` | `0xB6BE0` | 157 | UnwindData |  |
| 430 | `LocalSetForm` | `0xB6C90` | 142 | UnwindData |  |
| 434 | `SplAddForm` | `0xB6D30` | 129 | UnwindData |  |
| 449 | `SplDeleteForm` | `0xB6DC0` | 122 | UnwindData |  |
| 479 | `SplGetForm` | `0xB6E40` | 158 | UnwindData |  |
| 511 | `SplSetForm` | `0xB6EF0` | 142 | UnwindData |  |
| 447 | `SplCreatePrinterIC` | `0xB7340` | 79 | UnwindData |  |
| 459 | `SplDeletePrinterIC` | `0xB73A0` | 77 | UnwindData |  |
| 445 | `SplCopyFileEvent` | `0xBB840` | 179 | UnwindData |  |
| 446 | `SplCopyNumberOfFiles` | `0xBB900` | 150 | UnwindData |  |
| 502 | `SplLoadLibraryTheCopyFileModule` | `0xBB9A0` | 180 | UnwindData |  |
| 444 | `SplConfigChange` | `0xBBDF0` | 42 | UnwindData |  |
| 508 | `SplReportJobProcessingProgress` | `0xC87F0` | 118 | UnwindData |  |
| 406 | `SplEnumJobNamedProperties` | `0xD8220` | 111 | UnwindData |  |
| 506 | `SplPrintSupportOperation` | `0xDD420` | 637 | UnwindData |  |
| 495 | `SplIppCreateJobOnPrinter` | `0xDD760` | 571 | UnwindData |  |
| 496 | `SplIppCreateJobOnPrinterWithAttributes` | `0xDD9B0` | 609 | UnwindData |  |
| 497 | `SplIppGetJobAttributes` | `0xDDC20` | 550 | UnwindData |  |
| 498 | `SplIppGetPrinterAttributes` | `0xDDE50` | 494 | UnwindData |  |
| 499 | `SplIppSetJobAttributes` | `0xDE050` | 550 | UnwindData |  |
| 500 | `SplIppSetPrinterAttributes` | `0xDE280` | 494 | UnwindData |  |
