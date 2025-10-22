'use client'

import Image from 'next/image'

export default function Legal() {
    return (
        <main className="flex h-screen flex-col items-center font-sans overflow-x-hidden">
          <nav className="flex items-center justify-between w-screen bg-slate-100 p-5">
            <a href=".." className="text-gray-900 font-medium flex flex-row gap-2 items-center"><Image alt="TUM" src={"tum_logo.svg"} width={60} height={1}></Image>MQT QUBOMaker: Pathfinder</a>
            <a target="_blank" href="https://www.cda.cit.tum.de/research/quantum/" className="text-gray-900 font-medium hidden md:block">More on our Work</a>
            <a href="#" className="text-gray-900 font-medium hidden md:block">Legal Information</a>
            <a href="#" className="text-gray-900 font-medium block md:hidden"><Image alt="i" src={"info.png"} width={20} height={1}></Image></a>
          </nav>
          <div className="w-full h-full p-10 pl-[20%] pr-[20%] flex flex-col gap-5">
            <div>
              <div><b>Herausgeber</b></div>
              <div>Technische Universität München</div>
              <div>Arcisstraße 21</div>
              <div>80333 München</div>
              <div>Telefon: +49 89 289-01</div>
              <div>poststelle@tum.de</div>
            </div>

            <div>
              <div><b>Rechtsform und Vertretung</b></div>
              <div>Die Technische Universität München ist eine Körperschaft des Öffentlichen Rechts und staatliche Einrichtung (Art. 11 Abs. 1 BayHSchG). Sie wird gesetzlich vertreten durch den Präsidenten Prof. Dr. Thomas F. Hofmann.</div>
            </div>

            <div>
              <div><b>Zuständige Aufsichtsbehörde</b></div>
              <div>Bayerisches Staatsministerium für Wissenschaft und Kunst</div>
            </div>

            <div>
              <div><b>Umsatzsteueridentifikationnummer</b></div>
              <div>DE811193231 (gemäß § 27a Umsatzsteuergesetz)</div>
            </div>

            <div>
              <div><b>Inhaltlich verantwortlich</b></div>
              <div>Prof. Dr. Robert Wille</div>
              <div>Arcisstr. 21</div>
              <div>80333 München</div>
              <div>E-Mail: robert.wille(at)tum.de</div>
            </div>

            <div>
            Namentlich gekennzeichnete Internetseiten geben die Auffassungen und Erkenntnisse der genannten Personen wieder.
            </div>

            <div>
              <div><b>Nutzungsbedingungen</b></div>
              <div>Texte, Bilder, Grafiken sowie die Gestaltung dieses Webauftritts können dem Urheberrecht unterliegen. Nicht urheberrechtlich geschützt sind nach § 5 des Urheberrechtsgesetz (UrhG)</div>
              <ul>
              <li>- Gesetze, Verordnungen, amtliche Erlasse und Bekanntmachungen sowie Entscheidungen und amtlich verfasste Leitsätze zu Entscheidungen und</li>
              <li>- andere amtliche Werke, die im amtlichen Interesse zur allgemeinen Kenntnisnahme veröffentlicht worden sind, mit der Einschränkung, dass die Bestimmungen über Änderungsverbot und Quellenangabe in § 62 Abs. 1 bis 3 und § 63 Abs. 1 und 2 UrhG entsprechend anzuwenden sind.</li>
              </ul>
            </div>

            <div>
            Als Privatperson dürfen Sie urheberrechtlich geschütztes Material zum privaten und sonstigen eigenen Gebrauch im Rahmen des § 53 UrhG verwenden. Eine Vervielfältigung oder Verwendung urheberrechtlich geschützten Materials dieser Seiten oder Teilen davon in anderen elektronischen oder gedruckten Publikationen und deren Veröffentlichung ist nur mit unserer Einwilligung gestattet. Diese Einwilligung erteilen auf Anfrage die für den Inhalt Verantwortlichen. Der Nachdruck und die Auswertung von Pressemitteilungen und Reden sind mit Quellenangabe allgemein gestattet.
            </div>

            <div>
            Weiterhin können Texte, Bilder, Grafiken und sonstige Dateien ganz oder teilweise dem Urheberrecht Dritter unterliegen. Auch über das Bestehen möglicher Rechte Dritter geben Ihnen die für den Inhalt Verantwortlichen nähere Auskünfte.
            </div>

            <div>
              <div><b>Haftungsausschluss</b></div>
              <div>
              Alle in diesem Webauftritt bereitgestellten Informationen haben wir nach bestem Wissen und Gewissen erarbeitet und geprüft. Eine Gewähr für die jederzeitige Aktualität, Richtigkeit, Vollständigkeit und Verfügbarkeit der bereit gestellten Informationen können wir allerdings nicht übernehmen. Ein Vertragsverhältnis mit den Nutzern des Webauftritts kommt nicht zustande.
              </div>
            </div>

            <div>
            Wir haften nicht für Schäden, die durch die Nutzung dieses Webauftritts entstehen. Dieser Haftungsausschluss gilt nicht, soweit die Vorschriften des § 839 BGB (Haftung bei Amtspflichtverletzung) einschlägig sind. Für etwaige Schäden, die beim Aufrufen oder Herunterladen von Daten durch Schadsoftware oder der Installation oder Nutzung von Software verursacht werden, übernehmen wir keine Haftung.
            </div>

            <div>
              <div><b>Links</b></div>
              <div>
              Von unseren eigenen Inhalten sind Querverweise (&quot;Links&quot;) auf die Webseiten anderer Anbieter zu unterscheiden. Durch diese Links ermöglichen wir lediglich den Zugang zur Nutzung fremder Inhalte nach § 8 Telemediengesetz. Bei der erstmaligen Verknüpfung mit diesen Internetangeboten haben wir diese fremden Inhalte daraufhin überprüft, ob durch sie eine mögliche zivilrechtliche oder strafrechtliche Verantwortlichkeit ausgelöst wird. Wir können diese fremden Inhalte aber nicht ständig auf Veränderungen überprüfen und daher auch keine Verantwortung dafür übernehmen. Für illegale, fehlerhafte oder unvollständige Inhalte und insbesondere für Schäden, die aus der Nutzung oder Nichtnutzung von Informationen Dritter entstehen, haftet allein der jeweilige Anbieter der Seite.
              </div>
            </div>

            <div><br></br></div>
          </div>
        </main>
      );
}