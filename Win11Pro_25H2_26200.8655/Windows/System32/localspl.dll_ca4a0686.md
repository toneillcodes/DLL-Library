# Binary Specification: localspl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\localspl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ca4a0686558c2c8d39d05e605c97ea7dfad9fb2ed620a8159a5f576a434592fd`
* **Total Exported Functions:** 124

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 469 | `SplEnumPorts` | `0x121A0` | 172 | UnwindData |  |
| 504 | `SplOpenPrinter` | `0x140A0` | 151 | UnwindData |  |
| 477 | `SplEnumPrinters` | `0x14DB0` | 229 | UnwindData |  |
| 517 | `SplSetPrinterDataEx` | `0x24EA0` | 258 | UnwindData |  |
| 523 | `SplXcvData` | `0x2A110` | 188 | UnwindData |  |
| 475 | `SplEnumPrinterDrivers` | `0x2BFD0` | 174 | UnwindData |  |
| 490 | `SplGetPrinterDriverDirectory` | `0x301E0` | 154 | UnwindData |  |
| 482 | `SplGetPrintClassObject` | `0x30990` | 56 | UnwindData |  |
| 483 | `SplGetPrintClassObject_4CSR` | `0x309D0` | 140 | UnwindData |  |
| 451 | `SplDeleteMonitor` | `0x33280` | 142 | UnwindData |  |
| 494 | `SplGetUserPropertyBag` | `0x3D1F0` | 111 | UnwindData |  |
| 442 | `SplClosePrinter` | `0x3E5B0` | 88 | UnwindData |  |
| 515 | `SplSetPrinter` | `0x3F100` | 145 | UnwindData |  |
| 486 | `SplGetPrinter` | `0x40430` | 149 | UnwindData |  |
| 467 | `SplEnumJobs` | `0x43660` | 173 | UnwindData |  |
| 480 | `SplGetJob` | `0x43720` | 157 | UnwindData |  |
| 512 | `SplSetJob` | `0x437D0` | 149 | UnwindData |  |
| 429 | `LocalReadPrinter` | `0x44590` | 142 | UnwindData |  |
| 522 | `SplWritePrinter` | `0x451A0` | 142 | UnwindData |  |
| 407 | `SplGetDriverUpdateStatus` | `0x46F50` | 154 | UnwindData |  |
| 491 | `SplGetPrinterDriverEx` | `0x48F40` | 123 | UnwindData |  |
| 463 | `SplDriverEvent` | `0x4A0C0` | 141 | UnwindData |  |
| 421 | `DllMain` | `0x4DD70` | 792 | UnwindData |  |
| 448 | `SplCreateSpooler` | `0x4EE30` | 126 | UnwindData |  |
| 456 | `SplDeletePrinterData` | `0x51570` | 174 | UnwindData |  |
| 457 | `SplDeletePrinterDataEx` | `0x51630` | 183 | UnwindData |  |
| 474 | `SplEnumPrinterDataEx` | `0x516F0` | 155 | UnwindData |  |
| 487 | `SplGetPrinterData` | `0x517A0` | 221 | UnwindData |  |
| 488 | `SplGetPrinterDataEx` | `0x51890` | 166 | UnwindData |  |
| 516 | `SplSetPrinterData` | `0x51940` | 253 | UnwindData |  |
| 466 | `SplEnumForms` | `0x529F0` | 157 | UnwindData |  |
| 424 | `InitializePrintMonitor2` | `0x66830` | 574 | UnwindData |  |
| 505 | `SplPlayGdiScriptOnPrinterIC` | `0x68310` | 85 | UnwindData |  |
| 403 | `SplAddCSRPrinter` | `0x7DB50` | 161 | UnwindData |  |
| 404 | `SplDoesCSRPrinterDevnodeExist` | `0x7DC00` | 155 | UnwindData |  |
| 405 | `SplEnableCSRPrinterDeviceInterface` | `0x7DCB0` | 227 | UnwindData |  |
| 412 | `SplIsValidUserPropertyBag` | `0x7DDA0` | 113 | UnwindData |  |
| 440 | `SplAddPrinter` | `0x7F830` | 166 | UnwindData |  |
| 455 | `SplDeletePrinter` | `0x7F8E0` | 202 | UnwindData |  |
| 461 | `SplDeletePrinterWithJobs` | `0x7F9B0` | 129 | UnwindData |  |
| 507 | `SplRegeneratePrintDeviceCapabilities` | `0x7FA40` | 144 | UnwindData |  |
| 509 | `SplResetPrinter` | `0x7FAE0` | 122 | UnwindData |  |
| 409 | `SplGetLocalDevMode` | `0x81040` | 215 | UnwindData |  |
| 413 | `SplNotifyServerStatus` | `0x83480` | 237 | UnwindData |  |
| 415 | `SplSetCSRPrinterDevnode` | `0x83580` | 111 | UnwindData |  |
| 492 | `SplGetPrinterExtra` | `0x83600` | 122 | UnwindData |  |
| 493 | `SplGetPrinterExtraEx` | `0x83680` | 122 | UnwindData |  |
| 518 | `SplSetPrinterExtra` | `0x83700` | 122 | UnwindData |  |
| 519 | `SplSetPrinterExtraEx` | `0x83780` | 122 | UnwindData |  |
| 408 | `SplGetJobExtra` | `0x87CB0` | 192 | UnwindData |  |
| 417 | `SplSetJobError` | `0x87D80` | 335 | UnwindData |  |
| 418 | `SplSetJobExtra` | `0x87EE0` | 175 | UnwindData |  |
| 450 | `SplDeleteJobNamedProperty` | `0x89800` | 123 | UnwindData |  |
| 481 | `SplGetJobNamedPropertyValue` | `0x89890` | 135 | UnwindData |  |
| 513 | `SplSetJobNamedProperty` | `0x89920` | 123 | UnwindData |  |
| 401 | `LclIsSessionZero` | `0x89B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `LclPromptUIPerSessionUser` | `0x89B80` | 141 | UnwindData |  |
| 433 | `SplAbortPrinter` | `0x8D320` | 110 | UnwindData |  |
| 464 | `SplEndDocPrinter` | `0x8D3A0` | 181 | UnwindData |  |
| 465 | `SplEndPagePrinter` | `0x8D460` | 110 | UnwindData |  |
| 520 | `SplStartDocPrinter` | `0x8D560` | 182 | UnwindData |  |
| 521 | `SplStartPagePrinter` | `0x8D620` | 110 | UnwindData |  |
| 435 | `SplAddJob` | `0x8E770` | 149 | UnwindData |  |
| 510 | `SplScheduleJob` | `0x8E810` | 122 | UnwindData |  |
| 410 | `SplIsDriverInstalled` | `0x93620` | 129 | UnwindData |  |
| 411 | `SplIsLocalDriverAvailable` | `0x936B0` | 129 | UnwindData |  |
| 416 | `SplSetDriverUpdateStatus` | `0x93740` | 411 | UnwindData |  |
| 441 | `SplAddPrinterDriverEx` | `0x96020` | 158 | UnwindData |  |
| 458 | `SplDeletePrinterDriverEx` | `0x960D0` | 162 | UnwindData |  |
| 489 | `SplGetPrinterDriver` | `0x96180` | 67 | UnwindData |  |
| 501 | `SplIsCompatibleDriver` | `0x961D0` | 147 | UnwindData |  |
| 478 | `SplGetDriverDir` | `0x98A90` | 130 | UnwindData |  |
| 400 | *Ordinal Only* | `0x98B20` | 112 | UnwindData |  |
| 503 | `SplMonitorIsInstalled` | `0x98BA0` | 110 | UnwindData |  |
| 425 | `InitializePrintProvidor` | `0x9E7C0` | 118 | UnwindData |  |
| 443 | `SplCloseSpooler` | `0x9F850` | 110 | UnwindData |  |
| 462 | `SplDeleteSpooler` | `0x9FBB0` | 110 | UnwindData |  |
| 460 | `SplDeletePrinterKey` | `0xAB4B0` | 115 | UnwindData |  |
| 473 | `SplEnumPrinterData` | `0xAB530` | 188 | UnwindData |  |
| 476 | `SplEnumPrinterKey` | `0xAB600` | 147 | UnwindData |  |
| 414 | `SplReenumeratePorts` | `0xAD190` | 42 | UnwindData |  |
| 436 | `SplAddMonitor` | `0xAD820` | 141 | UnwindData |  |
| 437 | `SplAddPort` | `0xAD8C0` | 142 | UnwindData |  |
| 438 | `SplAddPortEx` | `0xAD960` | 149 | UnwindData |  |
| 452 | `SplDeletePort` | `0xADBC0` | 142 | UnwindData |  |
| 468 | `SplEnumMonitors` | `0xADC60` | 165 | UnwindData |  |
| 419 | `ClosePrintProcessor` | `0xB03B0` | 110 | UnwindData |  |
| 420 | `ControlPrintProcessor` | `0xB0430` | 122 | UnwindData |  |
| 422 | `EnumPrintProcessorDatatypesW` | `0xB04B0` | 166 | UnwindData |  |
| 423 | `GetPrintProcessorCapabilities` | `0xB0560` | 146 | UnwindData |  |
| 431 | `OpenPrintProcessor` | `0xB0600` | 124 | UnwindData |  |
| 432 | `PrintDocumentOnPrintProcessor` | `0xB0690` | 122 | UnwindData |  |
| 439 | `SplAddPrintProcessor` | `0xB0710` | 143 | UnwindData |  |
| 453 | `SplDeletePrintProcCacheData` | `0xB07B0` | 112 | UnwindData |  |
| 454 | `SplDeletePrintProcessor` | `0xB0830` | 142 | UnwindData |  |
| 470 | `SplEnumPrintProcCacheData` | `0xB08D0` | 127 | UnwindData |  |
| 471 | `SplEnumPrintProcessorDatatypes` | `0xB0960` | 174 | UnwindData |  |
| 472 | `SplEnumPrintProcessors` | `0xB0A20` | 174 | UnwindData |  |
| 484 | `SplGetPrintProcCacheData` | `0xB0AE0` | 147 | UnwindData |  |
| 485 | `SplGetPrintProcessorDirectory` | `0xB0B80` | 157 | UnwindData |  |
| 514 | `SplSetPrintProcCacheData` | `0xB0C30` | 139 | UnwindData |  |
| 426 | `LocalAddForm` | `0xB3010` | 141 | UnwindData |  |
| 427 | `LocalDeleteForm` | `0xB30B0` | 122 | UnwindData |  |
| 428 | `LocalEnumForms` | `0xB3130` | 157 | UnwindData |  |
| 430 | `LocalSetForm` | `0xB31E0` | 142 | UnwindData |  |
| 434 | `SplAddForm` | `0xB3280` | 129 | UnwindData |  |
| 449 | `SplDeleteForm` | `0xB3310` | 122 | UnwindData |  |
| 479 | `SplGetForm` | `0xB3390` | 158 | UnwindData |  |
| 511 | `SplSetForm` | `0xB3440` | 142 | UnwindData |  |
| 447 | `SplCreatePrinterIC` | `0xB3890` | 79 | UnwindData |  |
| 459 | `SplDeletePrinterIC` | `0xB38F0` | 77 | UnwindData |  |
| 445 | `SplCopyFileEvent` | `0xB7B90` | 179 | UnwindData |  |
| 446 | `SplCopyNumberOfFiles` | `0xB7C50` | 150 | UnwindData |  |
| 502 | `SplLoadLibraryTheCopyFileModule` | `0xB7CF0` | 180 | UnwindData |  |
| 444 | `SplConfigChange` | `0xB8060` | 42 | UnwindData |  |
| 508 | `SplReportJobProcessingProgress` | `0xC4220` | 118 | UnwindData |  |
| 406 | `SplEnumJobNamedProperties` | `0xD36E0` | 111 | UnwindData |  |
| 506 | `SplPrintSupportOperation` | `0xD8A10` | 766 | UnwindData |  |
| 495 | `SplIppCreateJobOnPrinter` | `0xD8DD0` | 571 | UnwindData |  |
| 496 | `SplIppCreateJobOnPrinterWithAttributes` | `0xD9020` | 609 | UnwindData |  |
| 497 | `SplIppGetJobAttributes` | `0xD9290` | 550 | UnwindData |  |
| 498 | `SplIppGetPrinterAttributes` | `0xD94C0` | 494 | UnwindData |  |
| 499 | `SplIppSetJobAttributes` | `0xD96C0` | 550 | UnwindData |  |
| 500 | `SplIppSetPrinterAttributes` | `0xD98F0` | 494 | UnwindData |  |
