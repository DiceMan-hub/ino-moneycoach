import React, { useState } from 'react';
import { LineChart, Line, AreaChart, Area, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const InstagramDashboard = () => {
  const rawData = {"visits": [{"Date": "2025-10-23", "Value": 596}, {"Date": "2025-10-24", "Value": 618}, {"Date": "2025-10-25", "Value": 646}, {"Date": "2025-10-26", "Value": 859}, {"Date": "2025-10-27", "Value": 537}, {"Date": "2025-10-28", "Value": 645}, {"Date": "2025-10-29", "Value": 492}, {"Date": "2025-10-30", "Value": 798}, {"Date": "2025-10-31", "Value": 504}, {"Date": "2025-11-01", "Value": 581}, {"Date": "2025-11-02", "Value": 613}, {"Date": "2025-11-03", "Value": 1077}, {"Date": "2025-11-04", "Value": 689}, {"Date": "2025-11-05", "Value": 664}, {"Date": "2025-11-06", "Value": 510}, {"Date": "2025-11-07", "Value": 689}, {"Date": "2025-11-08", "Value": 767}, {"Date": "2025-11-09", "Value": 806}, {"Date": "2025-11-10", "Value": 579}, {"Date": "2025-11-11", "Value": 1074}, {"Date": "2025-11-12", "Value": 625}, {"Date": "2025-11-13", "Value": 649}, {"Date": "2025-11-14", "Value": 547}, {"Date": "2025-11-15", "Value": 634}, {"Date": "2025-11-16", "Value": 496}, {"Date": "2025-11-17", "Value": 557}, {"Date": "2025-11-18", "Value": 525}, {"Date": "2025-11-19", "Value": 549}, {"Date": "2025-11-20", "Value": 430}, {"Date": "2025-11-21", "Value": 513}, {"Date": "2025-11-22", "Value": 425}, {"Date": "2025-11-23", "Value": 962}, {"Date": "2025-11-24", "Value": 551}, {"Date": "2025-11-25", "Value": 517}, {"Date": "2025-11-26", "Value": 521}, {"Date": "2025-11-27", "Value": 628}, {"Date": "2025-11-28", "Value": 410}, {"Date": "2025-11-29", "Value": 772}, {"Date": "2025-11-30", "Value": 394}, {"Date": "2025-12-01", "Value": 779}, {"Date": "2025-12-02", "Value": 489}, {"Date": "2025-12-03", "Value": 602}, {"Date": "2025-12-04", "Value": 461}, {"Date": "2025-12-05", "Value": 620}, {"Date": "2025-12-06", "Value": 480}, {"Date": "2025-12-07", "Value": 747}, {"Date": "2025-12-08", "Value": 529}, {"Date": "2025-12-09", "Value": 607}, {"Date": "2025-12-10", "Value": 418}, {"Date": "2025-12-11", "Value": 465}, {"Date": "2025-12-12", "Value": 362}, {"Date": "2025-12-13", "Value": 923}, {"Date": "2025-12-14", "Value": 487}, {"Date": "2025-12-15", "Value": 613}, {"Date": "2025-12-16", "Value": 375}, {"Date": "2025-12-17", "Value": 558}, {"Date": "2025-12-18", "Value": 305}, {"Date": "2025-12-19", "Value": 306}, {"Date": "2025-12-20", "Value": 303}, {"Date": "2025-12-21", "Value": 349}, {"Date": "2025-12-22", "Value": 435}, {"Date": "2025-12-23", "Value": 268}, {"Date": "2025-12-24", "Value": 358}, {"Date": "2025-12-25", "Value": 321}, {"Date": "2025-12-26", "Value": 481}, {"Date": "2025-12-27", "Value": 329}, {"Date": "2025-12-28", "Value": 623}, {"Date": "2025-12-29", "Value": 352}, {"Date": "2025-12-30", "Value": 502}, {"Date": "2025-12-31", "Value": 327}, {"Date": "2026-01-01", "Value": 699}, {"Date": "2026-01-02", "Value": 594}, {"Date": "2026-01-03", "Value": 625}, {"Date": "2026-01-04", "Value": 447}, {"Date": "2026-01-05", "Value": 607}, {"Date": "2026-01-06", "Value": 370}, {"Date": "2026-01-07", "Value": 548}, {"Date": "2026-01-08", "Value": 427}, {"Date": "2026-01-09", "Value": 486}, {"Date": "2026-01-10", "Value": 417}, {"Date": "2026-01-11", "Value": 493}, {"Date": "2026-01-12", "Value": 375}, {"Date": "2026-01-13", "Value": 505}, {"Date": "2026-01-14", "Value": 391}, {"Date": "2026-01-15", "Value": 500}, {"Date": "2026-01-16", "Value": 391}, {"Date": "2026-01-17", "Value": 670}, {"Date": "2026-01-18", "Value": 466}, {"Date": "2026-01-19", "Value": 909}, {"Date": "2026-01-20", "Value": 614}], "follows": [{"Date": "2025-10-23", "Value": 22}, {"Date": "2025-10-24", "Value": 9}, {"Date": "2025-10-25", "Value": 26}, {"Date": "2025-10-26", "Value": 16}, {"Date": "2025-10-27", "Value": 24}, {"Date": "2025-10-28", "Value": 15}, {"Date": "2025-10-29", "Value": 22}, {"Date": "2025-10-30", "Value": 20}, {"Date": "2025-10-31", "Value": 14}, {"Date": "2025-11-01", "Value": 15}, {"Date": "2025-11-02", "Value": 18}, {"Date": "2025-11-03", "Value": 23}, {"Date": "2025-11-04", "Value": 26}, {"Date": "2025-11-05", "Value": 26}, {"Date": "2025-11-06", "Value": 21}, {"Date": "2025-11-07", "Value": 26}, {"Date": "2025-11-08", "Value": 26}, {"Date": "2025-11-09", "Value": 34}, {"Date": "2025-11-10", "Value": 32}, {"Date": "2025-11-11", "Value": 33}, {"Date": "2025-11-12", "Value": 19}, {"Date": "2025-11-13", "Value": 21}, {"Date": "2025-11-14", "Value": 30}, {"Date": "2025-11-15", "Value": 27}, {"Date": "2025-11-16", "Value": 22}, {"Date": "2025-11-17", "Value": 20}, {"Date": "2025-11-18", "Value": 36}, {"Date": "2025-11-19", "Value": 25}, {"Date": "2025-11-20", "Value": 29}, {"Date": "2025-11-21", "Value": 17}, {"Date": "2025-11-22", "Value": 23}, {"Date": "2025-11-23", "Value": 51}, {"Date": "2025-11-24", "Value": 34}, {"Date": "2025-11-25", "Value": 22}, {"Date": "2025-11-26", "Value": 21}, {"Date": "2025-11-27", "Value": 24}, {"Date": "2025-11-28", "Value": 23}, {"Date": "2025-11-29", "Value": 15}, {"Date": "2025-11-30", "Value": 19}, {"Date": "2025-12-01", "Value": 22}, {"Date": "2025-12-02", "Value": 27}, {"Date": "2025-12-03", "Value": 39}, {"Date": "2025-12-04", "Value": 25}, {"Date": "2025-12-05", "Value": 25}, {"Date": "2025-12-06", "Value": 27}, {"Date": "2025-12-07", "Value": 43}, {"Date": "2025-12-08", "Value": 50}, {"Date": "2025-12-09", "Value": 34}, {"Date": "2025-12-10", "Value": 34}, {"Date": "2025-12-11", "Value": 30}, {"Date": "2025-12-12", "Value": 25}, {"Date": "2025-12-13", "Value": 52}, {"Date": "2025-12-14", "Value": 46}, {"Date": "2025-12-15", "Value": 59}, {"Date": "2025-12-16", "Value": 40}, {"Date": "2025-12-17", "Value": 40}, {"Date": "2025-12-18", "Value": 19}, {"Date": "2025-12-19", "Value": 24}, {"Date": "2025-12-20", "Value": 30}, {"Date": "2025-12-21", "Value": 25}, {"Date": "2025-12-22", "Value": 38}, {"Date": "2025-12-23", "Value": 16}, {"Date": "2025-12-24", "Value": 24}, {"Date": "2025-12-25", "Value": 14}, {"Date": "2025-12-26", "Value": 44}, {"Date": "2025-12-27", "Value": 26}, {"Date": "2025-12-28", "Value": 42}, {"Date": "2025-12-29", "Value": 36}, {"Date": "2025-12-30", "Value": 19}, {"Date": "2025-12-31", "Value": 21}, {"Date": "2026-01-01", "Value": 94}, {"Date": "2026-01-02", "Value": 73}, {"Date": "2026-01-03", "Value": 69}, {"Date": "2026-01-04", "Value": 61}, {"Date": "2026-01-05", "Value": 50}, {"Date": "2026-01-06", "Value": 43}, {"Date": "2026-01-07", "Value": 58}, {"Date": "2026-01-08", "Value": 30}, {"Date": "2026-01-09", "Value": 58}, {"Date": "2026-01-10", "Value": 35}, {"Date": "2026-01-11", "Value": 44}, {"Date": "2026-01-12", "Value": 38}, {"Date": "2026-01-13", "Value": 29}, {"Date": "2026-01-14", "Value": 35}, {"Date": "2026-01-15", "Value": 33}, {"Date": "2026-01-16", "Value": 31}, {"Date": "2026-01-17", "Value": 53}, {"Date": "2026-01-18", "Value": 33}, {"Date": "2026-01-19", "Value": 91}, {"Date": "2026-01-20", "Value": 70}], "interactions": [{"Date": "2025-10-23", "Value": 117}, {"Date": "2025-10-24", "Value": 515}, {"Date": "2025-10-25", "Value": 181}, {"Date": "2025-10-26", "Value": 334}, {"Date": "2025-10-27", "Value": 126}, {"Date": "2025-10-28", "Value": 428}, {"Date": "2025-10-29", "Value": 148}, {"Date": "2025-10-30", "Value": 410}, {"Date": "2025-10-31", "Value": 122}, {"Date": "2025-11-01", "Value": 311}, {"Date": "2025-11-02", "Value": 144}, {"Date": "2025-11-03", "Value": 353}, {"Date": "2025-11-04", "Value": 173}, {"Date": "2025-11-05", "Value": 208}, {"Date": "2025-11-06", "Value": 117}, {"Date": "2025-11-07", "Value": 240}, {"Date": "2025-11-08", "Value": 157}, {"Date": "2025-11-09", "Value": 492}, {"Date": "2025-11-10", "Value": 172}, {"Date": "2025-11-11", "Value": 343}, {"Date": "2025-11-12", "Value": 228}, {"Date": "2025-11-13", "Value": 465}, {"Date": "2025-11-14", "Value": 192}, {"Date": "2025-11-15", "Value": 264}, {"Date": "2025-11-16", "Value": 181}, {"Date": "2025-11-17", "Value": 589}, {"Date": "2025-11-18", "Value": 275}, {"Date": "2025-11-19", "Value": 300}, {"Date": "2025-11-20", "Value": 137}, {"Date": "2025-11-21", "Value": 342}, {"Date": "2025-11-22", "Value": 204}, {"Date": "2025-11-23", "Value": 465}, {"Date": "2025-11-24", "Value": 182}, {"Date": "2025-11-25", "Value": 448}, {"Date": "2025-11-26", "Value": 142}, {"Date": "2025-11-27", "Value": 247}, {"Date": "2025-11-28", "Value": 133}, {"Date": "2025-11-29", "Value": 661}, {"Date": "2025-11-30", "Value": 110}, {"Date": "2025-12-01", "Value": 368}, {"Date": "2025-12-02", "Value": 160}, {"Date": "2025-12-03", "Value": 1041}, {"Date": "2025-12-04", "Value": 357}, {"Date": "2025-12-05", "Value": 224}, {"Date": "2025-12-06", "Value": 167}, {"Date": "2025-12-07", "Value": 667}, {"Date": "2025-12-08", "Value": 328}, {"Date": "2025-12-09", "Value": 339}, {"Date": "2025-12-10", "Value": 169}, {"Date": "2025-12-11", "Value": 546}, {"Date": "2025-12-12", "Value": 173}, {"Date": "2025-12-13", "Value": 979}, {"Date": "2025-12-14", "Value": 409}, {"Date": "2025-12-15", "Value": 476}, {"Date": "2025-12-16", "Value": 365}, {"Date": "2025-12-17", "Value": 470}, {"Date": "2025-12-18", "Value": 146}, {"Date": "2025-12-19", "Value": 463}, {"Date": "2025-12-20", "Value": 209}, {"Date": "2025-12-21", "Value": 179}, {"Date": "2025-12-22", "Value": 297}, {"Date": "2025-12-23", "Value": 112}, {"Date": "2025-12-24", "Value": 610}, {"Date": "2025-12-25", "Value": 239}, {"Date": "2025-12-26", "Value": 378}, {"Date": "2025-12-27", "Value": 167}, {"Date": "2025-12-28", "Value": 470}, {"Date": "2025-12-29", "Value": 180}, {"Date": "2025-12-30", "Value": 258}, {"Date": "2025-12-31", "Value": 142}, {"Date": "2026-01-01", "Value": 801}, {"Date": "2026-01-02", "Value": 320}, {"Date": "2026-01-03", "Value": 560}, {"Date": "2026-01-04", "Value": 239}, {"Date": "2026-01-05", "Value": 797}, {"Date": "2026-01-06", "Value": 258}, {"Date": "2026-01-07", "Value": 487}, {"Date": "2026-01-08", "Value": 184}, {"Date": "2026-01-09", "Value": 824}, {"Date": "2026-01-10", "Value": 425}, {"Date": "2026-01-11", "Value": 401}, {"Date": "2026-01-12", "Value": 227}, {"Date": "2026-01-13", "Value": 639}, {"Date": "2026-01-14", "Value": 373}, {"Date": "2026-01-15", "Value": 422}, {"Date": "2026-01-16", "Value": 275}, {"Date": "2026-01-17", "Value": 649}, {"Date": "2026-01-18", "Value": 285}, {"Date": "2026-01-19", "Value": 788}, {"Date": "2026-01-20", "Value": 361}], "link_clicks": [{"Date": "2025-10-23", "Value": 53}, {"Date": "2025-10-24", "Value": 89}, {"Date": "2025-10-25", "Value": 288}, {"Date": "2025-10-26", "Value": 10}, {"Date": "2025-10-27", "Value": 17}, {"Date": "2025-10-28", "Value": 0}, {"Date": "2025-10-29", "Value": 0}, {"Date": "2025-10-30", "Value": 1}, {"Date": "2025-10-31", "Value": 38}, {"Date": "2025-11-01", "Value": 52}, {"Date": "2025-11-02", "Value": 19}, {"Date": "2025-11-03", "Value": 151}, {"Date": "2025-11-04", "Value": 131}, {"Date": "2025-11-05", "Value": 30}, {"Date": "2025-11-06", "Value": 6}, {"Date": "2025-11-07", "Value": 83}, {"Date": "2025-11-08", "Value": 117}, {"Date": "2025-11-09", "Value": 21}, {"Date": "2025-11-10", "Value": 54}, {"Date": "2025-11-11", "Value": 13}, {"Date": "2025-11-12", "Value": 80}, {"Date": "2025-11-13", "Value": 74}, {"Date": "2025-11-14", "Value": 4}, {"Date": "2025-11-15", "Value": 11}, {"Date": "2025-11-16", "Value": 65}, {"Date": "2025-11-17", "Value": 29}, {"Date": "2025-11-18", "Value": 74}, {"Date": "2025-11-19", "Value": 256}, {"Date": "2025-11-20", "Value": 98}, {"Date": "2025-11-21", "Value": 0}, {"Date": "2025-11-22", "Value": 0}, {"Date": "2025-11-23", "Value": 0}, {"Date": "2025-11-24", "Value": 0}, {"Date": "2025-11-25", "Value": 0}, {"Date": "2025-11-26", "Value": 126}, {"Date": "2025-11-27", "Value": 50}, {"Date": "2025-11-28", "Value": 7}, {"Date": "2025-11-29", "Value": 0}, {"Date": "2025-11-30", "Value": 13}, {"Date": "2025-12-01", "Value": 39}, {"Date": "2025-12-02", "Value": 52}, {"Date": "2025-12-03", "Value": 29}, {"Date": "2025-12-04", "Value": 0}, {"Date": "2025-12-05", "Value": 0}, {"Date": "2025-12-06", "Value": 149}, {"Date": "2025-12-07", "Value": 57}, {"Date": "2025-12-08", "Value": 0}, {"Date": "2025-12-09", "Value": 27}, {"Date": "2025-12-10", "Value": 32}, {"Date": "2025-12-11", "Value": 71}, {"Date": "2025-12-12", "Value": 110}, {"Date": "2025-12-13", "Value": 96}, {"Date": "2025-12-14", "Value": 0}, {"Date": "2025-12-15", "Value": 0}, {"Date": "2025-12-16", "Value": 0}, {"Date": "2025-12-17", "Value": 94}, {"Date": "2025-12-18", "Value": 24}, {"Date": "2025-12-19", "Value": 5}, {"Date": "2025-12-20", "Value": 47}, {"Date": "2025-12-21", "Value": 0}, {"Date": "2025-12-22", "Value": 7}, {"Date": "2025-12-23", "Value": 13}, {"Date": "2025-12-24", "Value": 0}, {"Date": "2025-12-25", "Value": 36}, {"Date": "2025-12-26", "Value": 21}, {"Date": "2025-12-27", "Value": 199}, {"Date": "2025-12-28", "Value": 116}, {"Date": "2025-12-29", "Value": 25}, {"Date": "2025-12-30", "Value": 20}, {"Date": "2025-12-31", "Value": 29}, {"Date": "2026-01-01", "Value": 38}, {"Date": "2026-01-02", "Value": 38}, {"Date": "2026-01-03", "Value": 49}, {"Date": "2026-01-04", "Value": 0}, {"Date": "2026-01-05", "Value": 9}, {"Date": "2026-01-06", "Value": 2}, {"Date": "2026-01-07", "Value": 9}, {"Date": "2026-01-08", "Value": 23}, {"Date": "2026-01-09", "Value": 57}, {"Date": "2026-01-10", "Value": 24}, {"Date": "2026-01-11", "Value": 0}, {"Date": "2026-01-12", "Value": 0}, {"Date": "2026-01-13", "Value": 0}, {"Date": "2026-01-14", "Value": 0}, {"Date": "2026-01-15", "Value": 4}, {"Date": "2026-01-16", "Value": 11}, {"Date": "2026-01-17", "Value": 190}, {"Date": "2026-01-18", "Value": 16}, {"Date": "2026-01-19", "Value": 38}, {"Date": "2026-01-20", "Value": 115}], "reach": [{"Date": "2025-10-23", "Value": 8331}, {"Date": "2025-10-24", "Value": 10182}, {"Date": "2025-10-25", "Value": 9122}, {"Date": "2025-10-26", "Value": 10725}, {"Date": "2025-10-27", "Value": 7031}, {"Date": "2025-10-28", "Value": 10617}, {"Date": "2025-10-29", "Value": 7705}, {"Date": "2025-10-30", "Value": 9571}, {"Date": "2025-10-31", "Value": 5915}, {"Date": "2025-11-01", "Value": 9212}, {"Date": "2025-11-02", "Value": 6925}, {"Date": "2025-11-03", "Value": 10939}, {"Date": "2025-11-04", "Value": 8328}, {"Date": "2025-11-05", "Value": 9604}, {"Date": "2025-11-06", "Value": 7151}, {"Date": "2025-11-07", "Value": 7689}, {"Date": "2025-11-08", "Value": 8601}, {"Date": "2025-11-09", "Value": 10717}, {"Date": "2025-11-10", "Value": 7555}, {"Date": "2025-11-11", "Value": 13317}, {"Date": "2025-11-12", "Value": 8993}, {"Date": "2025-11-13", "Value": 11255}, {"Date": "2025-11-14", "Value": 9504}, {"Date": "2025-11-15", "Value": 11508}, {"Date": "2025-11-16", "Value": 8538}, {"Date": "2025-11-17", "Value": 10081}, {"Date": "2025-11-18", "Value": 8475}, {"Date": "2025-11-19", "Value": 7824}, {"Date": "2025-11-20", "Value": 5891}, {"Date": "2025-11-21", "Value": 9037}, {"Date": "2025-11-22", "Value": 6796}, {"Date": "2025-11-23", "Value": 10889}, {"Date": "2025-11-24", "Value": 8301}, {"Date": "2025-11-25", "Value": 8940}, {"Date": "2025-11-26", "Value": 6229}, {"Date": "2025-11-27", "Value": 9124}, {"Date": "2025-11-28", "Value": 6462}, {"Date": "2025-11-29", "Value": 9434}, {"Date": "2025-11-30", "Value": 6313}, {"Date": "2025-12-01", "Value": 10653}, {"Date": "2025-12-02", "Value": 6756}, {"Date": "2025-12-03", "Value": 11547}, {"Date": "2025-12-04", "Value": 9659}, {"Date": "2025-12-05", "Value": 11660}, {"Date": "2025-12-06", "Value": 10049}, {"Date": "2025-12-07", "Value": 14397}, {"Date": "2025-12-08", "Value": 13679}, {"Date": "2025-12-09", "Value": 12385}, {"Date": "2025-12-10", "Value": 8172}, {"Date": "2025-12-11", "Value": 10997}, {"Date": "2025-12-12", "Value": 6929}, {"Date": "2025-12-13", "Value": 17211}, {"Date": "2025-12-14", "Value": 9818}, {"Date": "2025-12-15", "Value": 12275}, {"Date": "2025-12-16", "Value": 9193}, {"Date": "2025-12-17", "Value": 12748}, {"Date": "2025-12-18", "Value": 6562}, {"Date": "2025-12-19", "Value": 9531}, {"Date": "2025-12-20", "Value": 8042}, {"Date": "2025-12-21", "Value": 6798}, {"Date": "2025-12-22", "Value": 9262}, {"Date": "2025-12-23", "Value": 5854}, {"Date": "2025-12-24", "Value": 10133}, {"Date": "2025-12-25", "Value": 8151}, {"Date": "2025-12-26", "Value": 11025}, {"Date": "2025-12-27", "Value": 8081}, {"Date": "2025-12-28", "Value": 12115}, {"Date": "2025-12-29", "Value": 6974}, {"Date": "2025-12-30", "Value": 11274}, {"Date": "2025-12-31", "Value": 6281}, {"Date": "2026-01-01", "Value": 17479}, {"Date": "2026-01-02", "Value": 11269}, {"Date": "2026-01-03", "Value": 16998}, {"Date": "2026-01-04", "Value": 10050}, {"Date": "2026-01-05", "Value": 16117}, {"Date": "2026-01-06", "Value": 9585}, {"Date": "2026-01-07", "Value": 12706}, {"Date": "2026-01-08", "Value": 8190}, {"Date": "2026-01-09", "Value": 14365}, {"Date": "2026-01-10", "Value": 10156}, {"Date": "2026-01-11", "Value": 11982}, {"Date": "2026-01-12", "Value": 9774}, {"Date": "2026-01-13", "Value": 12748}, {"Date": "2026-01-14", "Value": 8952}, {"Date": "2026-01-15", "Value": 15168}, {"Date": "2026-01-16", "Value": 10715}, {"Date": "2026-01-17", "Value": 14333}, {"Date": "2026-01-18", "Value": 9898}, {"Date": "2026-01-19", "Value": 25322}, {"Date": "2026-01-20", "Value": 14920}], "views": [{"Date": "2025-10-23", "Value": 46595}, {"Date": "2025-10-24", "Value": 68785}, {"Date": "2025-10-25", "Value": 61916}, {"Date": "2025-10-26", "Value": 60261}, {"Date": "2025-10-27", "Value": 47821}, {"Date": "2025-10-28", "Value": 78149}, {"Date": "2025-10-29", "Value": 53105}, {"Date": "2025-10-30", "Value": 66810}, {"Date": "2025-10-31", "Value": 56264}, {"Date": "2025-11-01", "Value": 85009}, {"Date": "2025-11-02", "Value": 72665}, {"Date": "2025-11-03", "Value": 83663}, {"Date": "2025-11-04", "Value": 67762}, {"Date": "2025-11-05", "Value": 77605}, {"Date": "2025-11-06", "Value": 62303}, {"Date": "2025-11-07", "Value": 69395}, {"Date": "2025-11-08", "Value": 92296}, {"Date": "2025-11-09", "Value": 101988}, {"Date": "2025-11-10", "Value": 72991}, {"Date": "2025-11-11", "Value": 85936}, {"Date": "2025-11-12", "Value": 62364}, {"Date": "2025-11-13", "Value": 80670}, {"Date": "2025-11-14", "Value": 70350}, {"Date": "2025-11-15", "Value": 81145}, {"Date": "2025-11-16", "Value": 60576}, {"Date": "2025-11-17", "Value": 73521}, {"Date": "2025-11-18", "Value": 63566}, {"Date": "2025-11-19", "Value": 65547}, {"Date": "2025-11-20", "Value": 51387}, {"Date": "2025-11-21", "Value": 88094}, {"Date": "2025-11-22", "Value": 71741}, {"Date": "2025-11-23", "Value": 97573}, {"Date": "2025-11-24", "Value": 67032}, {"Date": "2025-11-25", "Value": 75646}, {"Date": "2025-11-26", "Value": 59397}, {"Date": "2025-11-27", "Value": 69158}, {"Date": "2025-11-28", "Value": 51344}, {"Date": "2025-11-29", "Value": 98899}, {"Date": "2025-11-30", "Value": 56109}, {"Date": "2025-12-01", "Value": 85129}, {"Date": "2025-12-02", "Value": 67948}, {"Date": "2025-12-03", "Value": 95391}, {"Date": "2025-12-04", "Value": 65256}, {"Date": "2025-12-05", "Value": 76008}, {"Date": "2025-12-06", "Value": 81453}, {"Date": "2025-12-07", "Value": 105495}, {"Date": "2025-12-08", "Value": 68788}, {"Date": "2025-12-09", "Value": 71879}, {"Date": "2025-12-10", "Value": 56825}, {"Date": "2025-12-11", "Value": 69051}, {"Date": "2025-12-12", "Value": 52506}, {"Date": "2025-12-13", "Value": 106547}, {"Date": "2025-12-14", "Value": 63308}, {"Date": "2025-12-15", "Value": 70531}, {"Date": "2025-12-16", "Value": 49831}, {"Date": "2025-12-17", "Value": 63011}, {"Date": "2025-12-18", "Value": 37863}, {"Date": "2025-12-19", "Value": 47881}, {"Date": "2025-12-20", "Value": 44944}, {"Date": "2025-12-21", "Value": 46678}, {"Date": "2025-12-22", "Value": 53111}, {"Date": "2025-12-23", "Value": 37214}, {"Date": "2025-12-24", "Value": 59399}, {"Date": "2025-12-25", "Value": 44629}, {"Date": "2025-12-26", "Value": 52888}, {"Date": "2025-12-27", "Value": 48968}, {"Date": "2025-12-28", "Value": 67390}, {"Date": "2025-12-29", "Value": 35425}, {"Date": "2025-12-30", "Value": 47561}, {"Date": "2025-12-31", "Value": 30081}, {"Date": "2026-01-01", "Value": 99813}, {"Date": "2026-01-02", "Value": 64269}, {"Date": "2026-01-03", "Value": 67840}, {"Date": "2026-01-04", "Value": 44141}, {"Date": "2026-01-05", "Value": 71007}, {"Date": "2026-01-06", "Value": 36751}, {"Date": "2026-01-07", "Value": 57424}, {"Date": "2026-01-08", "Value": 48590}, {"Date": "2026-01-09", "Value": 71879}, {"Date": "2026-01-10", "Value": 45569}, {"Date": "2026-01-11", "Value": 53194}, {"Date": "2026-01-12", "Value": 35444}, {"Date": "2026-01-13", "Value": 49694}, {"Date": "2026-01-14", "Value": 36065}, {"Date": "2026-01-15", "Value": 55871}, {"Date": "2026-01-16", "Value": 36338}, {"Date": "2026-01-17", "Value": 68431}, {"Date": "2026-01-18", "Value": 36299}, {"Date": "2026-01-19", "Value": 87505}, {"Date": "2026-01-20", "Value": 60217}]};

  // Combine data for overview chart
  const combinedData = rawData.visits.map((item, index) => ({
    date: item.Date.slice(5),
    訪問: rawData.visits[index].Value,
    フォロー: rawData.follows[index].Value,
    インタラクション: rawData.interactions[index].Value,
    リーチ: rawData.reach[index].Value / 100,
  }));

  // Calculate stats
  const calcStats = (data) => {
    const total = data.reduce((sum, item) => sum + item.Value, 0);
    const avg = Math.round(total / data.length);
    const recent7 = data.slice(-7).reduce((sum, item) => sum + item.Value, 0) / 7;
    const prev7 = data.slice(-14, -7).reduce((sum, item) => sum + item.Value, 0) / 7;
    const change = ((recent7 - prev7) / prev7 * 100).toFixed(1);
    return { total, avg, change, isPositive: parseFloat(change) >= 0 };
  };

  const stats = {
    visits: calcStats(rawData.visits),
    follows: calcStats(rawData.follows),
    interactions: calcStats(rawData.interactions),
    reach: calcStats(rawData.reach),
    views: calcStats(rawData.views),
    linkClicks: calcStats(rawData.link_clicks),
  };

  const StatCard = ({ title, icon, value, change, isPositive, avg }) => (
    <div className="bg-white rounded-xl p-6 shadow-lg hover:shadow-xl transition-shadow">
      <div className="text-sm text-gray-500 uppercase tracking-wide mb-2">{icon} {title}</div>
      <div className="text-3xl font-bold text-indigo-600 mb-2">{value.toLocaleString()}</div>
      <div className={`text-sm flex items-center gap-1 ${isPositive ? 'text-green-600' : 'text-red-600'}`}>
        <span>{isPositive ? '↗' : '↘'} {Math.abs(change)}%</span>
        <span className="text-gray-400">(直近7日間)</span>
      </div>
      <div className="text-xs text-gray-400 mt-2">1日平均: {avg.toLocaleString()}</div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 p-8">
      <div className="max-w-7xl mx-auto">
        <header className="text-center text-white mb-8">
          <h1 className="text-5xl font-bold mb-3 drop-shadow-lg">📊 Instagram Analytics Dashboard</h1>
          <p className="text-xl opacity-90">2025年10月23日 - 2026年1月20日</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <StatCard title="プロフィール訪問" icon="👥" {...stats.visits} />
          <StatCard title="フォロワー増加" icon="➕" {...stats.follows} />
          <StatCard title="インタラクション" icon="💬" {...stats.interactions} />
          <StatCard title="リーチ" icon="👁️" {...stats.reach} />
          <StatCard title="閲覧数" icon="📺" {...stats.views} />
          <StatCard title="リンククリック" icon="🔗" {...stats.linkClicks} />
        </div>

        <div className="bg-white rounded-xl p-6 shadow-xl mb-6">
          <h2 className="text-2xl font-bold mb-4 text-gray-800">📈 主要指標トレンド</h2>
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={combinedData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#e0e0e0" />
              <XAxis dataKey="date" tick={{fontSize: 12}} />
              <YAxis />
              <Tooltip
                contentStyle={{backgroundColor: 'rgba(255,255,255,0.95)', borderRadius: 8, border: '1px solid #ddd'}}
              />
              <Legend />
              <Line type="monotone" dataKey="訪問" stroke="#667eea" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="フォロー" stroke="#10b981" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="インタラクション" stroke="#f59e0b" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="リーチ" stroke="#8b5cf6" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl p-6 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-gray-800">👥 プロフィール訪問数</h2>
            <ResponsiveContainer width="100%" height={250}>
              <AreaChart data={rawData.visits.map(d => ({...d, date: d.Date.slice(5)}))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tick={{fontSize: 10}} />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="Value" stroke="#667eea" fill="#667eea" fillOpacity={0.3} />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="bg-white rounded-xl p-6 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-gray-800">➕ フォロワー増加</h2>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={rawData.follows.map(d => ({...d, date: d.Date.slice(5)}))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tick={{fontSize: 10}} />
                <YAxis />
                <Tooltip />
                <Bar dataKey="Value" fill="#10b981" />
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="bg-white rounded-xl p-6 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-gray-800">💬 インタラクション</h2>
            <ResponsiveContainer width="100%" height={250}>
              <AreaChart data={rawData.interactions.map(d => ({...d, date: d.Date.slice(5)}))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tick={{fontSize: 10}} />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="Value" stroke="#f59e0b" fill="#f59e0b" fillOpacity={0.3} />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="bg-white rounded-xl p-6 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-gray-800">👁️ リーチ</h2>
            <ResponsiveContainer width="100%" height={250}>
              <AreaChart data={rawData.reach.map(d => ({...d, date: d.Date.slice(5)}))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tick={{fontSize: 10}} />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="Value" stroke="#8b5cf6" fill="#8b5cf6" fillOpacity={0.3} />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InstagramDashboard;