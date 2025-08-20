// Ensure the chart container (.o_chart) is wider than viewport when needed
                const $chartContainer = this.$canvas.closest('.o_chart');
                if ($chartContainer && $chartContainer.length) {
                    let minWidth = 0;
                    const vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
                    const isTarget = (this.name === 'top_source' || this.name === 'best_team');
                    if (this.chart) {
                        const type = this.chart.config.type;
                        // Estimate width based on number of labels for bar-like charts
                        const labelsCount = (this.chart.data && this.chart.data.labels) ? this.chart.data.labels.length : 0;
                        if (type === 'bar' || type === 'horizontalBar') {
                            // Smaller per-label width and gentler viewport multiplier for Top Source/Best Team
                            const pxPerLabel = isTarget ? 40 : 48;
                            const vwMult = isTarget ? 1.02 : 1.06;
                            const cap = isTarget ? 1300 : 1500;
                            const base = isTarget ? 80 : 96;
                            minWidth = Math.max(vw * vwMult, Math.min(cap, labelsCount * pxPerLabel + base));
                        } else if (type === 'line') {
                            const vwMult = isTarget ? 1.02 : 1.06;
                            const cap = isTarget ? 1300 : 1500;
                            const base = isTarget ? 80 : 96;
                            const minBase = isTarget ? 660 : 680;
                            minWidth = Math.max(vw * vwMult, Math.min(cap, Math.max(minBase, labelsCount * 40 + base)));
                        } else if (type === 'pie' || type === 'doughnut') {
                            // Slightly wider than viewport for legends, but not too large
                            const vwMult = isTarget ? 1.01 : 1.02;
                            const minPx = isTarget ? 660 : 680;
                            minWidth = Math.max(vw * vwMult, minPx);
                        } else {
                            // Fallback
                            const vwMult = isTarget ? 1.02 : 1.06;
                            const minPx = isTarget ? 600 : 620;
                            minWidth = Math.max(vw * vwMult, minPx);
                        }
                    } else {
                        const vwMult = isTarget ? 1.02 : 1.06;
                        const minPx = isTarget ? 600 : 620;
                        minWidth = Math.max(vw * vwMult, minPx);
                    }
                    $chartContainer.css({ minWidth: Math.round(minWidth) + 'px', flex: '0 0 auto' });
                }
                // Nudge initial scroll slightly to the right to avoid left-edge clipping
                if ($boxContent && $boxContent.length) {
                    const current = $boxContent.scrollLeft();
                    if (current === 0) {
                        // A bit more nudge for Top Source/Best Team
                        const nudge = (this.name === 'top_source' || this.name === 'best_team') ? 16 : 12;
                        $boxContent.scrollLeft(nudge);
                    }
                }
                // Do not force height/width on canvas to keep aspect ratio intact